# calculate the sum of list of numbers

def rec_sum_list(l):
    if len(l) == 1:
        return l[0]
    else:
        return l[0] + rec_sum_list(l[1:])

print(rec_sum_list([1,2,3,4]))
