# implementing merge sort in ascending order

def mergesort(arr):
    # if len is one return the element
    if len(arr) <= 1:
        return arr

    # if len greater than one divide the array and make recursive call to both the arrays
    mid = len(arr) // 2
    left = arr[: mid]
    right = arr[mid:]
    mergesort(left)
    mergesort(right)

    # now compare the left list and right list elements and put it to original list
    #i for left array ,j for right array and k for new array where we store sorted elements
    i = j = k =0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
            k += 1
        else:
            arr[k] = right[j]
            k += 1
            j += 1

    # to print the left out elements in the left list
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    # to print the right most elements in the right list
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr

num = int(input("enter no of elements :"))
arr = [int(input()) for x in range(num)]
print("unsorted list is :",arr)
print("sorted list : ", mergesort(arr))

