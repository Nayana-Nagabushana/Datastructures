# inserting an element at given index

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# implementing the linked list class

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

# x - new node will inserted after the node x
    def insert_before_node(self,data,x):
        if self.head is None:
            print("linked list is empty")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        itr = self.head
        while itr:
            if itr.next.data == x:
                break
            itr = itr.next
        if itr.next is None:
            print("Node is not present in the linked list")
        else:
            new_node = Node(data)
            new_node.next = itr.next
            itr.next = new_node

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

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
    ll.insert_at_beginning(76)
    ll.print()
    ll.insert_before_node(100,10)
    ll.print()
