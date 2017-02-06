

def chunk_list(lst, size):
    result = []
    num = 0
    slice_len = size
    length = int(len(lst)/size)
    for i in range(0, length):
        result.append(lst[num:slice_len])
        num = slice_len
        slice_len = num+size
    if (len(lst)% size) > 0:
        result.append(lst[length*size:])
    print(result)
    


chunk_list(["a", "b", "c", "d"], 2)
chunk_list([0, 1, 2, 3, 4, 5, 6, 7, 8], 4)      
chunk_list([0, 1, 2, 3, 4, 5, 6, 7, 8], 2)
