def balanparenth(str):
    if len(str) % 2 != 0:
        return False
    opening = set("({[")
    matches = set([('(',')'),('[',']'),('{','}')])
    stack = []
    for ch in str:
        if ch in opening:
            stack.append(ch)
        else:
            if len(stack) == 0:
                return False

            last_open = stack.pop()

            if (last_open,ch) not in matches:
                return False
    return len(stack) == 0

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

print(balanparenth("{{()}}"))