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

    def search(self,data):
        n = self.head
        count = 0
        while n:
            if n.data == data:
                print("node is present in the list")
                break
            n = n.next
        if n is None:
            print("node is not present in the list")
            return


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
ll.search(23)
ll.search(100)
