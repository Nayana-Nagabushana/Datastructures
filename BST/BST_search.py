class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def search(self,data):
        if self.key == data:
            print("node found")
            return
        if self.key > data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("node is not present in the tree")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("node is not present in the tree")
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


root = BST(10)
lst = [5,13,8,33,0,1]
for i in lst:
    root.insert(i)
root.search(33)
