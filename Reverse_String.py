#Algorithm - step 1 -push all elements to stack
# step 2 :pop all the elements and reverse it until the bottom of the stack
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

def ReverseString(sentence):
    stack = Stack()
    for word in sentence:
        stack.push(word)
    rstr = ''
    while stack.size() != 0:
        rstr += stack.pop()
    return rstr

print(ReverseString("My name is nayana"))
