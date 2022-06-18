from collections import OrderedDict
choiceDict =None
class Graph:
    def __init__(self):
        self.vertex = OrderedDict()

    def addEdge(self):
        fromVertex = input("ENTER THE FROM VERTEX")
        toVertex      = input("ENTER THE TO VERTEX")
        if fromVertex in self.vertex.keys():
            self.vertex[fromVertex].append(toVertex)
        else:
            self.vertex[fromVertex] = [toVertex]

    def displayGraph(self):
        for vertex  in self.vertex.keys():
            print(vertex, ' -> [', ' -> '.join([str(j) for j in self.vertex[vertex]]),']')

def main():

    print("*" * 20)
    graph = Graph()
    choiceDict = {
        1: graph.addEdge,
        2: graph.displayGraph,
        3: exit
    }
    while(1):
        print("\t\t1: Insert edge in the graph\n")
        print("\t\t2: Display graph\n")
        choice = int(input("Choice:"))
        choiceDict[choice]()



if __name__ == '__main__':
    main()
