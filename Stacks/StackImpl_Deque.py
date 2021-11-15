# implementing stack using deque

from collections import deque

stack = deque()
stack.append(1)
stack.append(2)
stack.append(5)
stack.append(9)

print(stack)

stack.pop()
stack.pop()
print(stack)