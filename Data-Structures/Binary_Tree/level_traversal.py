# Python program to traverse a binary tree as per the levels

from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left  = None
        self.right = None

    def insert(self, data):
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

    def level_traversal(self):
        if self == None: return
        dq = deque()
        numNodes = 0
        level = 0
        dq.append(self)
        while dq:

            front = dq[0]
            if front.left != None: dq.append(front.left)
            if front.right != None: dq.append(front.right)
            node = dq.popleft()
            print(node.data)
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

    node.level_traversal()        
