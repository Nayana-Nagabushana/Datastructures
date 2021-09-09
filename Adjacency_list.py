'''
for implementing adjacency list we take 2 classes - Vertex(represents each vertex in graph) and
graph(master list os vertices)
connectedTo dictionary keeps track of the vertices to which it is connected and weight of eah edge
addNeighbor - to add connection from one vertex to another
getConnections - to get all the vertices in adjacency list
getWeight - returns the weight of the edge
'''

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight = 0):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

    def __str__(self):
        return str(self.id) +  " connected to :"  + str([x.id for x in self.connectedTo])


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


g = Graph()
for i in range(6):
    g.addVertex(i)

g.vertList

g.addEdge(0,1,2)
for vertex in g:
    print (vertex)
    print (vertex.getConnections())
    print ('\n')