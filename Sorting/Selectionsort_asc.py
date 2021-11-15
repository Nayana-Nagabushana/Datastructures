# implement selection sort using min() method
# len(arr) or len(arr)-1 can be given

def selectionsort(arr):

    for i in range(len(arr)):
        min_value = min(arr[i:])
        min_index = arr.index(min_value)
        if arr[i] != arr[min_index]:      #this condition is given bcz if the elements are in the correct position
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr = [3,55,1,0,8,9,23,-1]
print(selectionsort(arr))
