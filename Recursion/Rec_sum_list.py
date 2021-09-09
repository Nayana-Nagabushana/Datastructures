# return the sum of list - n = n + (n-2) + (n-4)

def sum_list(n):
    if n < 1:
        return 0
    else:
        return n + sum_list(n - 2)


print(sum_list(6))