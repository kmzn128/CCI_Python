class Node:
    
    def __init__(self, item):
        self.item = item
        self.visited = False
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
    #node.visited = True

def dfs(node):
    if(not node):
        return
    if(node.left):# and not node.left.visited):
        dfs(node.left)
    visit(node)
    if(node.right):# and not node.right.visited):
        dfs(node.right)

#dfs(root)

from collections import deque

def bfs(node):
    queue = deque([])
    queue.append(node)
    while(len(queue) > 0):
        n = queue.popleft()
        visit(n)
        if(n.left):# and not n.left.visited):
            queue.append(n.left)
        if(n.right):# and not n.right.visited):
            queue.append(n.right)

bfs(root)