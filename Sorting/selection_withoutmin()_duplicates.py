# implement selection sort  without using min() method

def selectionsort(arr):
    for i in range(len(arr)-1):
        m_ind = i
        for j in range(i+1,len(arr)):
            if  arr[j] < arr[m_ind]:
                m_ind = j
        arr[i], arr[m_ind] = arr[m_ind], arr[i]
    return arr

arr = [3,55,1,0,8,9,23,-1]
print(selectionsort(arr))
