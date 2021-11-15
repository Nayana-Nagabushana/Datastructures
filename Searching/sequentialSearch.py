# program to find the key element in linear array

def linear_search(arr, key):
    for position in range(len(arr)):
        if key == arr[position]:
            print("element {} found at index {}".format(key,position))
            break;
    else:
        print("element not found")


arr = [5,8,12,9,3,45,10]
linear_search(arr,46)