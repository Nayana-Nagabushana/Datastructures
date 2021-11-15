class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            n = self.head
            while n.next:
                n = n.next
            n.next = new_node

    def print(self):
        if self.head is None:
            print("list is empty")
            return
        else:
            n = self.head
            llstr = " "
            while n:
                llstr += str(n.data) + "--->"
                n = n.next
            print(llstr)

ll = Linkedlist()
ll.insert(10)
ll.print()
ll.insert(20)
ll.print()
ll.insert(100)
ll.print()
