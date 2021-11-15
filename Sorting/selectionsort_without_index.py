# implement selection sort  without using index method

def selectionsort(arr):
    for i in range(len(arr)-1):
        m_index = i
        for j in range(i+1,len(arr)):
            if  arr[j] < arr[m_index]:
                m_index = j
        if i != m_index:
            arr[i], arr[m_index] = arr[m_index], arr[i]
    return arr

arr = [3,55,1,0,8,9,23,-1]
print(selectionsort(arr))
