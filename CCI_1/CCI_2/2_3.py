from linked_list import LinkedList

ll = LinkedList()

for i in range(10):
    ll.appendToTail(i)

curr = ll.head
half_runner = ll.head
flip = False
while(curr.next):
    if(flip):
        flip = False
        half_runner = half_runner.next
    else:
        flip = True
    curr = curr.next
ll.remove_by_node(half_runner)

ll.list_print()


