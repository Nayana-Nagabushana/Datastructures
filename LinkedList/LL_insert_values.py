# creating a new linked list using the data list provided

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# implementing the linked list class

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_values(self,data_list):
        for data in data_list:
            self.insert_at_end(data)

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)

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
    ll.insert_values(["Apple","Banana","Cherry","Doritos"])
    ll.print()

