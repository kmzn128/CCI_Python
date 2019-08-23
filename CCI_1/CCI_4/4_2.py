import random
int_list = [i for i in range(10)]

class Node:

    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def insert(root, node):
    if(root.val > node.val):
        if(root.left == None):
            root.left = node
        else:
            insert(root.left, node)
    else:
        if(root.right == None):
            root.right = node
        else:
            insert(root.right, node)

tree_root = Node(int_list[0])
for i in range(1,10):
    insert(tree_root, Node(int_list[i]))

def inorder(root): 
    if root: 
        inorder(root.left) 
        print(root.val) 
        inorder(root.right) 

#inorder(tree_root)

def preorder(root):
    if(root != None):
        print(root.val)
        preorder(root.left)
        preorder(root.right)

#preorder(tree_root)
new_list_for_bst = []

def _mmdt(_list, start, end):
    if(start > end):
        return
    center_idx = (start+end)//2
    new_list_for_bst.append(_list[center_idx])
    _mmdt(_list, start, center_idx-1)
    _mmdt(_list, center_idx+1, end)

def make_minimal_depth_tree(_list):
    _mmdt(_list, 0, len(_list)-1)

def find_center_idx(_list):
    return len(_list)//2
make_minimal_depth_tree(int_list)
print(new_list_for_bst)
    
    

