# fibonacci using iteration and recursion

def rec_fib_itr(n):
    a,b =0,1
    for i in range(n):
        a,b = b,a+b
    return a

print(rec_fib_itr(10))

def rec_fib_recr(n):
    if n == 0 or n == 1:
        return n
    return rec_fib_recr(n-1) + rec_fib_recr(n-2)

print(rec_fib_recr(10))
