# implement selection sort  without using min() method

def selectionsort(arr):
    for i in range(len(arr)-1):
        m_value = arr[i]
        for j in range(i+1,len(arr)):
            if  arr[j] < m_value:
                m_value = arr[j]
        m_index = arr.index(m_value)
        arr[i], arr[m_index] = arr[m_index], arr[i]
    return arr

arr = [3,55,1,0,8,9,23,-1]
print(selectionsort(arr))
