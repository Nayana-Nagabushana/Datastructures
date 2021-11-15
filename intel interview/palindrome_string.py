def palindrome(s):
    res_str = ''
    for i in s:
        res_str = i + res_str
    if res_str == s:
        return True
    else:
        return False


print(palindrome('madam'))
print(palindrome('madama'))