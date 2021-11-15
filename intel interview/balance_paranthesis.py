def paranthesis(s):
    if len(s) % 2 != 0:
        return False
    open = set('({[')
    matches = set([('(',')'),('[',']'),('{','}')])
    stack = []
    for paren in s:
        if paren in open:
            stack.append(open)
        else:
            if len(stack) == 0:
                return False
            last_open = stack.pop()
            print(last_open)
            if (last_open, paren) not in matches:
                return False
    return len(stack) == 0

print(paranthesis('[]({{}})'))