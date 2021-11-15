# reverse string using recursion

def rev_string(s):
    #base case
    if len(s) <= 1:
        return s

    #recursive case
    return rev_string(s[1:]) + s[0]

print(rev_string('nayana'))