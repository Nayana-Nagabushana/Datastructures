# implementing insertion sort
# we dont consider first element, so we start iterating from index 1 to whole length of the array
# will compare each element in the unsorted list with the sorted list

def insertionSort(arr):
    for index in range(1, len(arr)):
        current_element = arr[index]
        while current_element < arr[index - 1] and index > 0:
            arr[index] = arr[index - 1]
            index -= 1
        arr[index] = current_element
    return arr


elements = [9, 10, 2, 0, 5, 4 , -1]
print(insertionSort(elements))
