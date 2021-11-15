# removing the element at the specified index

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# implementing the linked list class

class LinkedList:
    def __init__(self):
        self.head = None

    def delete_at_beginning(self):
        if self.head is None:
            print("list is empty")
        else:
            self.head = self.head.next

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(43)
    ll.insert_at_beginning(7)
    ll.print()
    ll.delete_at_beginning()
    ll.print()
    ll.delete_at_beginning()
    ll.print()
