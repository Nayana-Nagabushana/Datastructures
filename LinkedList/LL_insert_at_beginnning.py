# implementing the node -contains data(string,integer,etc) next - pointer to the next node

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# implementing the linked list class

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

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
    ll.insert_at_beginning(1991)
    ll.insert_at_beginning(12)
    ll.insert_at_beginning(5)
    ll.print()

