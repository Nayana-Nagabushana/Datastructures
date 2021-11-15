#balance paranthesis using stack

def ismatch(ch1,ch2):
    match_dict = { ")": "(","]" : "[","}": "{"}
    return match_dict[ch1] == ch2

def balancedParanthesis(input1):
    stack = []
    for symbol in input1:
        if symbol in ["(","[","{"]:
            stack.append(symbol)
        if symbol in [")","]","}"]:
            if len(stack)== 0:
                return False
            if not ismatch(symbol,stack.pop()):
                return False
    return len(stack) == 0



print(balancedParanthesis("({})"))
print(balancedParanthesis("{[{()}}"))