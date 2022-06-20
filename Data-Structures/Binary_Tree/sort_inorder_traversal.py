class Node:
    def __init__(self, data):
        self.data   = data
        self.left    = None
        self.right = None

    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            if data > self.data:
                if self.right == None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.data, end=' ')
        if self.right is not None:
            self.right.inorder()
