class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    


    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_val(self, node):
        
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node
        self.length += 1

    def print(self):
        current_node = self.head
        for i in range(self.length):
              print(current_node.val)
              if(i != 0):
                current_node = current_node.next


        

ll = LinkedList()

for i in range(10):
    ll.add_val(Node(i+10))
ll.print()
