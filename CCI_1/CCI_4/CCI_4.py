class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.visited = False

class Graph:
    def __init__(self):
        self.nodes = []

    def _sub_search(self, root, _to):
        if(root == None):
            return False
        root.visited = True
        if(root == _to):
            return True
        for child in root.children:
            if(child.visited == False):
                self._sub_search(child, _to)    

    def search(self, _from, _to):
        pass
       
a = Node(0)
b = Node(1)
c = Node(2)
d = Node(3)
e = Node(4)
f = Node(5)
g = Node(6)

a.children = [b]
b.children = [c]
c.children = [a,d]
d.children = [c]
e.children = [f]
f.children = [g]
g.children = [e]

graph = Graph()
graph.nodes = [a,b,c,d,e,f,g]

print(graph.search(a,d))
