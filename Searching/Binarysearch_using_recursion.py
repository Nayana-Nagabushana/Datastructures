# implement a binary search using recursion
# recursion functions will not have loops

def rec_bin_search(arr , key):
    if len(arr) == 0:
        return False
    else:
        mid = len(arr)//2
        if key == arr[mid]:
            return True
        else:
            if key > arr[mid]:
                return rec_bin_search(arr[mid+1:], key)
            else:
                return rec_bin_search( arr[ : mid],key)



arr = [1,5,6,8,12,19,24,60]
print(rec_bin_search(arr ,9))