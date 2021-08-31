from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.appendleft(item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == 0
