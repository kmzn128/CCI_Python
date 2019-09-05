class Node:
    
    def __init__(self, item):
        self.item = item
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

def visit(node):
    print(node.item)

def next(node):
    if(not node):
        return
    if(node.left):
        next(node.left)
    visit(node)
    if(node.right):
        next(node.right)

next(root)

