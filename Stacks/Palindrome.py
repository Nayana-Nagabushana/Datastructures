#implementing palindrome - step 1 push all charatcers to stack
#pop each charctaer and comapre with that of the character in string
def palindrome(str):
    mystack = Stack()
    palin= False
    for char in str:
        mystack.push(char)
    for char in str:
        if char == mystack.pop():
            palin = True
        else:
            palin = False
    return palin

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

print(palindrome('NAYAN'))
print(palindrome('NAYANA'))
