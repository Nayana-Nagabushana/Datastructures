class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr)

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_by_value(self, value):
        if self.head is None:
            print("Cant delete empty linked list")
            return
        if value == self.head.data:
            self.head = self.head.next
            return
        itr = self.head
        while itr.next:
            if value == itr.next.data:
                break
            itr = itr.next
        if itr.next is None:
            print("node is not present")
        else:
            itr.next = itr.next.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(45)
    ll.insert_at_beginning(2)
    ll.insert_at_beginning(10)
    ll.print()
    ll.delete_by_value(2)
    ll.print()
