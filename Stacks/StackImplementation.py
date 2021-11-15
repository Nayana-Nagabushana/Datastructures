#implementing stack using Arrays/lists

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


mystack = Stack()
mystack.push("A")
mystack.push(2)
mystack.push("hello world")
print(mystack.size())

mystack.pop()
mystack.pop()
print(mystack.size())
print(mystack.peek())

mystack.pop()
print(mystack.size())

mystack.pop()

