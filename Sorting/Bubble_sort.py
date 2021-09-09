# sorting the arrays using bubble sort
# we use a flag swapped to check if the elements are sorted
# we give size - 1- i because each iteration we wont consider the sorted element

def bubble_sort(elements):
    size = len(elements)

    for i in range(size - 1):
        swapped = False
        for j in range(size - 1 -i):
            if elements[j] > elements[j+1]:
                temp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = temp
                swapped = True

        if not swapped:
            break

if __name__ == '__main__':
    elements = [9,3,6,1,2]
    bubble_sort(elements)
    print(elements)