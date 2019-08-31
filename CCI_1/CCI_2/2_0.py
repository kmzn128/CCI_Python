class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def appendToTail(self, data):
        end = Node(data)
        if(self.head == None):
            self.head = end
            return
        curr = self.head
        while(curr.next != None):
            curr = curr.next
        curr.next = end

    def remove(self, data):
        if(self.head == None):
            return
        prev = None
        curr = self.head
        while(curr.data != data):
            prev = curr
            curr = curr.next
        if(curr.data == data):
            prev.next = curr.next
        return

ll = LinkedList()
ll.appendToTail(0)
ll.appendToTail(1)
ll.appendToTail(2)
ll.remove(1)
ll.appendToTail(3)
ll.appendToTail(4)
    