# program to return the cumulative sum of a given number
# example - n=4 4+3+2+1+0 = 10

def rec_sum(n):

    #base case
    if n == 0:
        return 0
    else:
        return n + rec_sum(n-1)

print(rec_sum(4))