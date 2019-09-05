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

targetSum = 6

def find_target_sum(targetSum):
    pass