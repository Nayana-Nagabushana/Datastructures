# program to find the key element in sorted linear array

def linear_search(arr, key):
    for position in range(len(arr)):
        if arr[position] > key:
            print("element not found")
            break
        elif key == arr[position]:
            print("element {} found at index {}".format(key,position))
            break


arr = [2,5,6,7,8,9,10]
linear_search(arr,3)