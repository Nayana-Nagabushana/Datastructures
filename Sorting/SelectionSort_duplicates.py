# implement selection sort using min() method
# giving i after min_value gives the first occurance of the minimum value
#u can give len(arr) or len(arr)-1

def selectionsort(arr):
    for i in range(len(arr)-1):      #-1 can be given because there will be only one element left
        min_value = min(arr[i:])
        min_index = arr.index(min_value,i)
        if arr[i] != arr[min_index]:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr = [56,0,2,2,0,6]
print(selectionsort(arr))
