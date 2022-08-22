import subprocess

import pytest
import sys
import os
import stat
import pdb
sys.path.append("..")
from src.find_1st_match_file import find_1st_file


def fake_file(file_path, file_size):
    with open(file_path, 'wb') as f:
        f.write(os.urandom(file_size))
    f.close()


def make_executable(path):
    mode = os.stat(path).st_mode
    mode |= (mode & 0o444) >> 2    # copy R bits to X
    os.chmod(path, mode)


def set_file_mode_exec(fname):
    st = os.stat(fname)
    print("mode is:", st.st_mode)
    os.chmod(fname, st.st_mode | stat.S_IEXEC)


@pytest.fixture()
def my_heleprs():
    print("\n<< setup")
    yield
    # pdb.set_track()
    if os.path.isfile(os.getcwd()+os.sep+'data'+os.sep+"testfile.x"):
        print("=== found ===")
        os.remove(os.getcwd()+os.sep+'data'+os.sep+"testfile.x")
        print(" REMOVED ")

    print("\n teardown>>")


def test_find_match_has_a_match(my_heleprs):
    # Clear the content folder
    # build a content folder
    #
    # run the test.
    current_dir = os.getcwd()
    print(current_dir+os.sep+'data')
    file_path = os.getcwd() + os.sep + 'data' + os.sep + "testfile.x"
    fake_file(file_path, 14680064-1)
    make_executable(file_path)
    subprocess.check_call(['chmod', '+x', file_path])
    name = find_1st_file(current_dir+os.sep+"data")
    print("file found is :", name)
    assert name is not None


def test_find_match_has_no_match_size(my_heleprs):
    # create a file set has not matching
    current_dir = os.getcwd()
    file_path = os.getcwd() + os.sep + 'data' + os.sep + "testfile.xy"
    fake_file(file_path, 14680064)
    name = find_1st_file(current_dir + os.sep + "data")
    # print("file found is :", name)
    assert name is None

