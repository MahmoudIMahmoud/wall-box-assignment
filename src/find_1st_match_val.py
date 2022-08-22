from pydoc import doc


def first_match(arr1,arr2):
    """_summary_
    Args:
        arr1 (_type_): _description_
        arr2 (_type_): _description_
    Returns:
        The index and the value in a firtstly found in b
        index to be -1 when no matches found.
    """
    index = -1
    value = -1
    for idx in range(len(arr1)):
        if arr1[idx] in arr2:
            return idx,arr1[idx]
    return index,value

# if __name__=="__main__":
#     a = [1,2,3]
#     b = [7,4,5]
#     index,value = first_match(a,b)
#     if index>-1: 
#         print(f"found a match {value} at index {index}")
#     else:
#         print("no matches found ....")