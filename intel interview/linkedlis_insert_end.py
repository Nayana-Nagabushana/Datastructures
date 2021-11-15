class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)

    def print(self):
        if self.head is None:
            print("list is empty")
            return
        itr = self.head
        lst = ''
        while itr:
            lst += str(itr.data) + "--->"
            itr = itr.next
        print(lst)


ll = Linkedlist()
ll.insert_at_beginning(10)
ll.print()
ll.insert_at_beginning(20)
ll.print()
ll.insert_at_end(100)
ll.print()
