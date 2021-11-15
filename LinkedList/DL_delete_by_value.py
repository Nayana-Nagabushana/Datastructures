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

    def delete_by_value(self,x):
        if self.head is None:
            print("list is empty")
            return
        if self.head.next is None:
            if x == self.head.data:
                self.head = None
            else:
                print("x is not present in list")
            return
        if self.head.data == x:
            self.head = self.head.next
            self.head.prev = None
            return
        itr = self.head
        while itr.next is not None:
            if x == itr.data:
                break
            itr = itr.next
            if itr.next is not None:
                itr.next.prev = itr.prev
                itr.prev.next = itr.next
            else:
                if itr.data == x:
                    itr.prev.next = None
                else:
                    print("x is not present in linked lst")




dl = doublylist()
dl.insert_beginning(20)
dl.insert_beginning(30)
dl.insert_beginning(40)
dl.insert_beginning(12)
dl.insert_beginning(10)
dl.print_ll()
dl.delete_by_value(12)
dl.print_ll()
dl.delete_by_value(40)
dl.print_ll()
dl.delete_by_value(5)