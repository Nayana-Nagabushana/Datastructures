def palindrome(num):
    rev = 0
    result = num
    while num != 0:
        dig = num % 10
        rev = rev * 10 + dig
        num //= 10
    if rev == result:
        return True
    else:
        return False


print(palindrome(343))
print(palindrome(521))