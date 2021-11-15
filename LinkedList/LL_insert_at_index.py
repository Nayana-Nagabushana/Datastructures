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

    def insert_at_index(self,index,data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_beginning(data)

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(data)
                node.next = itr.next
                itr.next = node
                break
            itr = itr .next
            count += 1

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
    ll.insert_at_beginning(12)
    ll.insert_at_beginning(34)
    ll.insert_at_beginning(20)
    ll.insert_at_beginning(50)
    ll.print()
    ll.insert_at_index(0,'Figs')
    ll.print()
    ll.insert_at_index(2, 'Jackfruit')
    ll.print()

