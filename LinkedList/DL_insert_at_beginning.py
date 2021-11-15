class Node:
    def __init__(self, data):
        self.data  = data
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

    def insert_empty(self, data):     # insert a node when list is empty
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("linked list is not empty")

    def insert_beginning(self, data):   # insert a node at the beginning of the list
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node


dl = doublylist()
#dl.insert_empty(10)
#dl.print_ll()
#dl.insert_empty(5)
dl.insert_beginning(20)
dl.print_ll()
dl.insert_beginning(30)
dl.print_ll()
dl.insert_beginning(40)
dl.print_ll()