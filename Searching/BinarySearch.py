# function to find a key using binary search

def binarysearch(arr, key):
    low = 0
    high = len(arr) - 1
    found = False
    while low <= high and not found:
        mid = (low + high)//2
        if key == arr[mid]:
            found = True
        elif key > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    if found:
        print("key found")
    else:
        print("key not found")

arr = [10,9,23,5,1,0,44,98]
arr.sort()
print(arr)
key = int(input("enter the key : "))
binarysearch(arr ,key)