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

def visit(node):
    print(node.item)

count = 0
def check_node_num(node):
    global count
    if(not node):
        return
    count += 1
    if(node.left):
        check_node_num(node.left)
    if(node.right):
        check_node_num(node.right)
    return

check_node_num(root)
print(count)

def find_inorder_successor(node):
    pass

