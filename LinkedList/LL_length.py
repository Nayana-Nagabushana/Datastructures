# To find the length of the linked list


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# implementing the linked list class

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1      # count each node and increment it
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
    ll.insert_values(["Apple","Banana","Cherry","Doritos","Grapes"])
    ll.print()
    print("length : ",ll.get_length())

