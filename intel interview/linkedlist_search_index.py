# pgm to return the Nth node in the list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            n = self.head
            while n.next:
                n = n.next
            n.next = new_node

    def search_index(self, index):
        if index < 0 or index >= self.get_length():
            print("Invalid index")
            return

        n = self.head
        count = 0
        while n:
            if count == index:
                print(n.data)
                break
            count += 1
            n =n.next
        if n is None:
            print("node is not present in the list")
            return

    def get_length(self):
        n = self.head
        count = 0
        while n:
            count += 1
            n = n.next
        return count

    def print(self):
        if self.head is None:
            print("list is empty")
            return
        else:
            n = self.head
            llstr = " "
            while n:
                llstr += str(n.data) + "--->"
                n = n.next
            print(llstr)

ll = Linkedlist()
ll.insert(10)
ll.insert(20)
ll.insert(100)
ll.print()
ll.search_index(1)
ll.search_index(0)
ll.search_index(2)
ll.search_index(4)
