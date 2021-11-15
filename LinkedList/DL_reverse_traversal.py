class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr)

    def print_backward(self):        # for printing reverse order we need to find the last node
        if self.head is None:
            print("Linked list is empty")
            return

        last_node = self.get_last_node()               # we get last node from last node function
        itr = last_node
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.prev
        print(llstr)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count

    def insert_at_begining(self, data):  # insert a node at the beginning of the list
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node


if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert_at_begining(12)
    ll.insert_at_begining(30)
    ll.insert_at_begining(40)
    ll.insert_at_begining(100)
    ll.insert_at_begining(23)
    ll.print_forward()
    ll.print_backward()
