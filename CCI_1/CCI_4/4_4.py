class Node:
    
    def __init__(self, item):
        self.item = item
        #self.visited = False
        self.depth = 1
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

def visit(parent, node):
    if(parent):
        node.depth = parent.depth + 1
    print("item:{0}, depth:{1}".format(node.item, node.depth))
    #node.visited = True

def dfs(parent, node):
    if(not node):
        return
    visit(parent, node)
    if(node.left):# and not node.left.visited):d
        dfs(node, node.left)
    if(node.right):# and not node.right.visited):
        dfs(node, node.right)

#dfs(None, root)

def max_depth(node):
    if(not node):
        return 0
    left_depth = right_depth = 0
    if(node.left):
        left_depth = max_depth(node.left)
    if(node.right):
        right_depth = max_depth(node.right)
    return max(left_depth, right_depth) + 1

#print(max_depth(root))

def check_balanced(node):
    if(not node):
        return True
    left_depth = right_depth = 0
    if(node.left):
        left_depth = max_depth(node.left)
    if(node.right):
        right_depth = max_depth(node.right)
    if(abs(left_depth - right_depth) > 1):
        return False
    else:
        return True

def whole_check_balanced(node):
    left_check = right_check = True
    if(node.left):
        left_check = check_balanced(node.left)
    if(node.right):
        right_check = check_balanced(node.right)
    return left_check and right_check

print(check_balanced(root))