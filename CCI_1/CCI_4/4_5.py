
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
root.left = e
root.right = b
 
def check_bst(node):
    if(not node):
        return True
    if(node.left):
        if(node.left.item < node.item):
            check_bst(node.left)
        else:
            return False
    if(node.right):
        if(node.right.item > node.item):
            check_bst(node.right)
        else:
            return False
    return True

print(check_bst(root))