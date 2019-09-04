from linked_list import LinkedList

input_list = [0,1,2,2,2,3,3,3,4,5,6,6,6]
ll = LinkedList()
for elem in input_list:
    ll.appendToTail(elem)
ll.list_print()

def dup():
    curr = ll.head
    dup_checker = set()
    while(curr.next):
        if(curr.data not in dup_checker):
            dup_checker.add(curr.data)
        else:
            ll.remove(curr.data)
        curr = curr.next
    ll.list_print()

def no_dup():
    curr = ll.head.next
    runner = ll.head
    while(curr.next):
        while(runner.next is not curr.next):
            if(runner.data == curr.data):
                ll.remove(curr.data)
                runner = ll.head
            else:
                runner = runner.next
        curr = curr.next
    ll.list_print()

no_dup()
    




