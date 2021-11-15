# implementing insertion sort in descending order
# we dont consider first element, so we start iterating from index 1 to whole length of the array
# will compare each element in the unsorted list with the sorted list

def insertionSort(arr):
    for index in range(1,len(arr)):
        current_element = arr[index]
        pos = index
        while current_element > arr[pos - 1] and pos >0:
            arr[pos] = arr[pos - 1]
            pos -= 1
        arr[pos] = current_element
    return arr

elements = [9,10,2,0,5,4]
print(insertionSort(elements))
