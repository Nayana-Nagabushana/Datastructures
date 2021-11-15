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

    def delete_at_end(self):
        if self.head is None:
            print("list is empty")
            return
        elif self.head.next is None:
            self.head = None
        else:
            itr = self.head
            while itr.next.next:
                itr = itr.next
            itr.next = None

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
ll.insert_at_beginning(20)
ll.insert_at_beginning(40)
ll.insert_at_beginning(55)
ll.print()
ll.delete_at_end()
ll.print()
ll.delete_at_end()
ll.print()
