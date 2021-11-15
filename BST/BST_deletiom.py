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
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key)
        if self.rchild:
            self.rchild.inorder()


    def delete(self,data,curr):
        if self.key is None:
            print("Tree is empty")
            return
        if self.key > data:
            if self.lchild:
                self.lchild = self.lchild.delete(data,curr)
            else:
                print("given node is not present in the tree")
        elif self.key < data:
            if self.rchild:
                self.rchild = self.rchild.delete(data,curr)
            else:
                print("given node is not present in the tree")
        else:
            if self.lchild is None:
                temp = self.rchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                self = None
                return temp
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.delete(node.key)
        return self

def count(node):
    if node is None:
        return 0
    return 1 + count(node.lchild) + count(node.rchild)

root = BST(10)
lst = [5,13,8,33,0,1]
for i in lst:
    root.insert(i)
print(count(root))
if count(root) > 1:
    root.delete(10,root.key,curr)
else:
    print("cant perform deletion")
