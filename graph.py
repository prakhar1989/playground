class Vertex(object):
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + \
                str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

class Graph(object):
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def __contains__(self, n):
        return n in self.vertList

    def __iter__(self):
        return iter(self.vertList.values())

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        return self.vertList.get(n)

    def getVertices(self):
        return self.vertList.keys()

    def addEdge(self, u, v, cost=0):
        if u not in self.vertList:
            nv = self.addVertex(u)
        if v not in self.vertList:
            nv = self.addVertex(v)
        self.vertList[u].addNeighbor(self.vertList[v], cost)


if __name__ == "__main__":
    g = Graph()
    for i in range(6):
        g.addVertex(i)

    g.addEdge(0, 1)
    g.addEdge(0, 5)
    g.addEdge(1, 2)

    for i in g:
        print i
