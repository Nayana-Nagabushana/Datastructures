# permutation of the string given
# example s= abc should return [abc,acb,bac,bca,cab,cba]

def perm_string(s):
    out = []
    if len(s) == 1:
        out = [s]

    for i,letter in enumerate(s):
        for perm in perm_string(s[:i] + s[i+1 :]):
            out += [letter + perm]
    return out

print(perm_string('abc'))
