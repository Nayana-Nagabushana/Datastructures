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

    def insert_beginning(self, data):   # insert a node at the beginning of the list
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_after(self , data, x):    # new node to be inserted after the node x
        if self.head is None:
            print("linked list is empty")
        else:
            itr = self.head
            while itr:
                if itr.data == x:
                    break
                itr = itr.next
            if itr is None:
                print("node is not present in doubly linked list")
            else:
                new_node = Node(data)
                new_node.next = itr.next
                new_node.prev = itr
                if itr.next is not None:
                    itr.next.prev = new_node
                itr.next = new_node

dl = doublylist()
dl.insert_beginning(20)
dl.insert_beginning(30)
dl.insert_beginning(40)
dl.insert_beginning(100)
dl.insert_beginning(23)
dl.print_ll()
dl.insert_after(5, 40)
dl.print_ll()