# return the index of the duplicate elements in the array

def lin_search(arr1,key):
    list2 = []
    flag = False
    for i in range(len(arr1)):
        if key == arr1[i]:
            flag = True
            list2.append(i)
    if flag == True:
        print("key element  found at index :")
        for i in list2:
            print(i, end = " , ")
    else:
        print("key element not found")

arr1 = [1,7,6,6,6,6,6,6,68]
lin_search(arr1,6)