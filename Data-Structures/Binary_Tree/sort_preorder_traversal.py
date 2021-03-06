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

    def preorder(self):
        if self.right is not None:
            self.right.preorder()
        print(self.data, end=' ')
        if self.left is not None:
            self.left.preorder()

def main():
    node = Node(50)

    node.insert(20)
    node.insert(60)
    node.insert(65)
    node.insert(5)
    node.insert(10)
    node.insert(3)
    node.insert(300)
    node.insert(400)
    node.insert(500)
    
    print(" SORTED TREE Using Inorder Traversal \n"
    node.preorder()
