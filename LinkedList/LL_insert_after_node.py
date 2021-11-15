# inserting an element at given index

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# implementing the linked list class

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

# x - new node will inserted after the node x
    def insert_after_node(self,data,x):
        itr = self.head
        while itr:
            if x == itr.data:
                break
            itr = itr.next
        if itr is None:
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
    ll.insert_at_beginning(24)
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(2)
    ll.print()
    ll.insert_after_node(100,10)
    ll.insert_after_node(56, 103)
    ll.print()
