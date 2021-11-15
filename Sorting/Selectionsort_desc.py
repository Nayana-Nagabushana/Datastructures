# implement selection sort using  max() method to sort in descendiing order

def selectionsort(arr):
    for i in range(len(arr)):
        max_value = max(arr[i:])
        max_index = arr.index(max_value)
        if arr[i] != arr[max_index]:
            arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr

arr = [3,55,1,0,8,9,23,-1]
print(selectionsort(arr))
