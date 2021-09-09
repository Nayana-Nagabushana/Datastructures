#balance paranthesis using stack

def ismatch(ch1,ch2):
    match_dict = { ")": "(","]" : "[","}": "{"}
    return match_dict[ch1] == ch2

def balancedParanthesis(input1):
    mystack = Stack()
    for symbol in input1:
        if symbol in ["(","[","{"]:
            mystack.push(symbol)
        if symbol in [")","]","}"]:
            if mystack.size == 0:
                return False
            if not ismatch(symbol,mystack.pop()):
                return False
    return mystack.size() == 0

class Stack(object):
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if self.items == []:
            print("Stack underflow")
        else:
            return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[len(self.items)-1]

    def isEmpty(self):
        return self.items == []


print(balancedParanthesis("({a+b})"))
print(balancedParanthesis("(()))"))
print(balancedParanthesis("{{()}}"))