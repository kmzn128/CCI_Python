class Node:
    
    def __init__(self, item):
        self.item = item
        #self.visited = False
        #self.depth = 1
        self.left = None
        self.right = None


root = Node(3)
b = Node(2)
c = Node(1)
d = Node(4)
e = Node(5)
f = Node(6)

b.left = c
e.left = d
e.right = f
root.left = b
root.right = e

def traverse(node):
    if node is not None:
        yield from traverse(node.left)
        yield node.item
        yield from traverse(node.right)

print(traverse(root))