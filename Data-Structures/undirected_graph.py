from collections import OrderedDict
from collections import  defaultdict
from pprint import pprint
choiceDict =None

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visitedNodes = defaultdict(bool)

    def addEdge(self):
        fromVertex = input("ENTER THE FROM VERTEX")
        toVertex      = input("ENTER THE TO VERTEX")
        self.vertex[toVertex].append(fromVertex)
        self.vertex[fromVertex].append(toVertex)
        self.visitedNodes[fromVertex]=False
        self.visitedNodes[toVertex]=False
        print ("\n\nGRAPH -> ")
        pprint(self.vertex)
        print("\n")

    def detectCycle(self):

        # Marked all nodes as visited, dfsVisited as False

        for node in self.graph:
            if self.visitedNodes[node] == False:
                if self.isCyclic(node, self.visitedNodes):
                    print ("Graph has a cycle")
                    return True
        print("Graph has a NO CYCLE")
        return False

    def isCyclic(self, node, visitedNodes, parent=None):
        visitedNodes[node] = True

        if node in self.graph:
            for neighbour in self.graph[node]:
                    if visitedNodes[neighbour] == False:
                        if self.isCyclic(neighbour, visitedNodes, ):
                            return True
                    elif self.dfsVisitedNodes[neighbour] == True:
                        # Cycle detected , as 'DFS visited' is true
                        return True
        self.dfsVisitedNodes[node] = False
        return False

    def displayGraph(self):
        for vertex  in self.vertex.keys():
            print(vertex, ' -> [', ' -> '.join([str(j) for j in self.vertex[vertex]]),']')

    def deleteGraph(self):
        self.vertex = OrderedDict()
def main():

    print("*" * 20)
    graph = Graph()
    choiceDict = {
        1: graph.addEdge,
        2: graph.displayGraph,
        3: graph.detectCycle,
        4: graph.deleteGraph,
        5: exit
    }
    while(1):
        print("\t\t1: Insert edge in the undirected graph\n")
        print("\t\t2: Display graph\n")
        print("\t\t3: Detect cycle\n")
        print("\t\t4: Delete Graph\n")
        print("\t\t5: Exit\n")
        choice = int(input("Choice:"))
        retVal = choiceDict[choice]()



if __name__ == '__main__':
    main()
