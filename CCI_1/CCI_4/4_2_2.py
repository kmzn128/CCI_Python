class Node:
    
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

def insert(root, item):
    if(item < root.item):
        if(root.left == None):
            root.left = item
        else:
            insert(root.left, item)
    else:
        if(root.right == None):
            root.right = item
        else:
            insert(root.right, item)




