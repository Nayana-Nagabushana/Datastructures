def reverse(s):
    res_str = ''
    for alphabet in s:
        res_str = alphabet + res_str
    return res_str


print(reverse('nayana'))