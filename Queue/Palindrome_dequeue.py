#implementing palindrome using dequeue

def palindrome(str):
    q = Dequeue()
    stillEqual = True
    for char in str:
        q.addRear(char)
    while q.size() > 1 and stillEqual:
        first = q.removeFront()
        last = q.removeRear()
        if first != last:
            stillEqual = False
    return stillEqual



class Dequeue:
    def __init__(self):
        self.items = []

    def addRear(self,item):
        self.items.insert(0,item)

    def addFront(self,item):
        self.items.append(item)

    def removeRear(self):
        return self.items.pop(0)

    def removeFront(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

print(palindrome('NAYAN'))
print(palindrome("HELLO"))