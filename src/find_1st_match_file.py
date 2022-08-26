import os
from pathlib import Path
import pdb
file_size = 14*2**20


def is_exec(file_path):
    return os.path.isfile(file_path) and os.access(file_path, os.X_OK)


def is_admin_owned(file_path):
    return os.stat(file_path).st_uid == 0


def get_size(file_path):
    return os.stat(file_path).st_size


def find_1st_file(dir_path):
    '''
    :param dir_path:
    :return:
    - None if nothing is found.
    - File name if the file was found.
    '''
    print(dir_path, os.sep)
    # pdb.set_track()
    print(dir_path)
    contents = os.listdir(dir_path)
    for entry in contents:
        # print(entry)
        file_path = dir_path+os.sep+entry
        # file_path = Path.resolve(file_path)
        print(file_path)
        if is_admin_owned(file_path):
            print("is_admin_owned")
            if is_exec(file_path):
                print("is_exec")
                if get_size(file_path) < file_size:
                    print("size check")
                    return file_path
        return None
