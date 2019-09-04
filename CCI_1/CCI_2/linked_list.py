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
        while((curr != None) and (curr.data != data) ):
            prev = curr
            curr = curr.next
        if(curr == None):
            return
        if(curr.data == data):
            prev.next = curr.next
        return
    
    def remove_by_node(self, node):
        if(self.head == None):
            return
        prev = None
        curr = self.head
        while((curr != None) and (curr is not node) ):
            prev = curr
            curr = curr.next
        if(curr == None):
            return
        if(curr is node):
            prev.next = curr.next
        return

    def find(self, data):
        if(not self.head):
            return None
        curr = self.head
        while(curr and (curr.data != data)):
            curr = curr.next
        if(not curr):
            return None
        if(curr.data == data):
            return curr
        return None

    def insert(self, data, pos):
        inserted = Node(data)
        if(not pos.next):
            pos.next = inserted
        else:
            next_node = pos.next
            pos.next = inserted
            inserted.next = next_node

    def list_print(self):
        li = []
        if(not self.head):
            return
        curr = self.head
        while(curr.next):
            li.append(str(curr.data))
            li.append(" > ")
            curr = curr.next
        li.append(str(curr.data))
        print("".join(li))

#ll = LinkedList()
#def test_insert():

#    ll.appendToTail(0)
#    ll.appendToTail(1)
#    ll.appendToTail(2)
#    node_1 = ll.find(1)
#    ll.insert(3, node_1)

#test_insert()
#ll.list_print()



    