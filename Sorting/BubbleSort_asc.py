# sorting the arrays using bubble sort in ascending order
# we use a flag swapped to check if the elements are sorted
# we give size - 1- i because each iteration we wont consider the sorted element

def bubble_sort_asc(elements):
    for i in range(len(elements)-1):
        for j in range(len(elements)-1-i):
            if elements[j] > elements[j+1]:
                elements[j],elements[j+1] = elements[j+1], elements[j]
    print("sorted list :" ,elements)

elements = []
num = int(input("enter the number of elements to sort : "))
print("enter the values : ")
for k in range(num):
    elements.append(int(input()))
print("unsorted list : ",elements)
bubble_sort_asc(elements)


