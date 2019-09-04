from linked_list import LinkedList

input_list = [0,1,2,2,2,3,3,3,4,5,6,6,6]
ll = LinkedList()
for elem in input_list:
    ll.appendToTail(elem)
ll.list_print()

l2 = LinkedList()
def return_kth(k):
    i = 0
    curr = ll.head
    while(curr.next):
        if(i<k):
            i += 1
            curr = curr.next
            continue
        l2.appendToTail(curr.data)
        curr = curr.next
    l2.appendToTail(curr.data)

return_kth(4)
l2.list_print()
