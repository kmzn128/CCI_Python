from linked_list import LinkedList

ll = LinkedList()

input_list = [3,5,8,10,8,5,4]

for i in input_list:
    ll.appendToTail(i)
    
reversed_ll = LinkedList()
for i in input_list:
    reversed_ll.appendToTail(i)


reversed_ll.reverse()
reversed_ll.list_print()

    