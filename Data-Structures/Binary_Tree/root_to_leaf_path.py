# Program to print the path from root to leaf nodes
from pdb import set_trace as st
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
            data = dq.popleft()
            numNodes +=1

            if numNodes == 1 and level ==0:
                print(f"{data.data}")
                numNodes=0
                level +=1
                st()
                expectedNodesAtLevel = 2**level
                print("\n\n")
            else:
                print(f"{data.data}")
                if numNodes == expectedNodesAtLevel:
                    print("\n\n")
                    numNodes = 0
                    level += 1
                    expectedNodesAtLevel = 2 ** level


   

    def pathFromRootToLeaf(self):

        if self == None: return
        root = self
        visited = deque()
        dfs        = deque()
        visited.append(self)
        dfs.append(self)
        currentNode = self
        while visited:

            # If current Node is leaf node
            if currentNode.left == None and currentNode.right==None:
                #Print the path
                for node in dfs:
                    print(node.data)
                st()
                print("\n\n")
                # It is a leaf node so mark as visited
                visited.append(currentNode)
                # Pop the child node from dfs
                dfs.pop()
                # Make the parent of child as current node
                currentNode = dfs[len(dfs)-1]

            # Make current node as right node if its not visited
            if currentNode.left == None and currentNode.right != None and currentNode.right not in visited  or \
                currentNode.left in visited and currentNode.right not in visited and currentNode.right != None:
                currentNode = currentNode.right
                if currentNode not in dfs: dfs.append(currentNode)
            # Make current node as left  node if its not visited
            elif currentNode.right == None and currentNode.left != None and currentNode.left not in visited or \
                currentNode.right in visited   and currentNode.left not in visited and currentNode.left != None:
                currentNode = currentNode.left
                if currentNode not in dfs:          dfs.append(currentNode)

            # Make current node as visited if both child nodes are visited
            if currentNode.left in visited and currentNode.right in visited or\
                    currentNode.left  in visited and currentNode.right ==None or \
                    currentNode.right  in visited and currentNode.left ==None:
                st()
                dfs.pop()
                visited.append(currentNode)
                currentNode = dfs[len(dfs) - 1]


            if currentNode.left != None  and currentNode.right != None:
                st()
                if currentNode.left not in visited:
                    currentNode = currentNode.left
                elif currentNode.right not in visited:
                    currentNode = currentNode.right
                dfs.append(currentNode)
                visited.append(currentNode)

            if currentNode.left in visited and currentNode.right in visited and currentNode == root:
                st()
                visited = []



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

    #print(" SORTED TREE Using Inorder Traversal \n")
    #node.inorder()

    #node.level_traversal()
    node.pathFromRootToLeaf()

if __name__ == '__main__':
    main()
