# to find the index of all occurances in the sorted list
# numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
# number_to_find = 15
#This should return 5,6,7 as indices containing number 15 in the array

# program to find the key element in linear array

# function to find a key using binary search

def binarysearch(arr, key):
    low = 0
    high = len(arr) - 1
    found = False
    mid = None
    lst = []
    while low <= high and not found:
        mid = (low + high)//2
        if key == arr[mid]:
            found = True
        elif key > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    lst.append(mid)
    md = mid
    mid -= 1
    while  mid >= 0 :
        if key == arr[mid]:
            lst.append(mid)
            mid -= 1
        else:
            break
    mid = md
    mid += 1
    while mid <= len(arr):
        if key == arr[mid]:
            lst.append(mid)
            mid += 1
        else:
            break
    print(lst)




arr = [1,4,6,9,11,15,15,15,17,21,34,34,56]
arr.sort()
print(arr)
key = int(input("enter the key : "))
binarysearch(arr ,key)