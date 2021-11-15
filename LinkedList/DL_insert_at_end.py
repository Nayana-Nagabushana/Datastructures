class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class doublylist:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print("linked list is empty")
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + "--->"
            itr = itr.next
        print(llstr)

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            itr = self.head
            while itr.next is not None:
                itr = itr.next
            itr.next = new_node
            new_node.prev = itr


dl = doublylist()
dl.insert_end(20)
dl.print_ll()
dl.insert_end(100)
dl.print_ll()
dl.insert_end(13)
dl.print_ll()
