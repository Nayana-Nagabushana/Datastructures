# function to return sum of digits
# example - n =4321 4+3+2+1=10

def sum_func(n):
    if len(str(n)) == 1:
        return n
    else:
        return n%10 + sum_func(n/10)

print(sum_func(4321))