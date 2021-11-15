class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    def min_node(self):
        current = self
        while current.lchild:
            current = current.lchild
        print("node with smallest key is :",current.key)

    def max_node(self):
        current = self
        while current.rchild:
            current = current.rchild
        print("node with largest key is :",current.key)

root = BST(10)
lst = [5,13,8,33,0,1]
for i in lst:
    root.insert(i)
root.min_node()
root.max_node()
