# two strings are anagram if both string can be formed exactly with same letters
# dog and god,man and nam

def anagram_check(s1 , s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    if len(s1) != len(s2):
        return False
    count = {}
    for a in s1:
        if a not in count:
            count[a] = 1
        else:
            count[a] +=1
    for b in s2:
        if b not in count:
            count[b] = 1
        else:
            count[b] -= 1

    for k in count:
        if count[k] != 0:
            return False
    return True

print(anagram_check("dd","aa"))
print(anagram_check("dog","god"))
print(anagram_check("is a day","today"))