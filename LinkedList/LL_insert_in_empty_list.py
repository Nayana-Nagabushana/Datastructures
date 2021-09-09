# inserting node when list is empty

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

    def insert_in_empty_list(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked list is not empty")


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
    ll.insert_in_empty_list(20)
    ll.print()
    ll.insert_in_empty_list(100)


