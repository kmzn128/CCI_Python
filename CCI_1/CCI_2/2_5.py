from linked_list import LinkedList

ll_a = LinkedList()
ll_b = LinkedList()

a_value = [7,1,6]
b_value = [5,9,2]

for i in a_value:
    ll_a.appendToTail(i)
for i in b_value:
    ll_b.appendToTail(i)

ll_a.list_print()
ll_b.list_print()

def make_num(linked_list):
    if(not linked_list.head):
        return -1
    curr = linked_list.head
    digit = 0
    sum = 0
    while(curr):
        sum += curr.data * (10 ** digit)
        curr = curr.next
        digit += 1
    return sum

a = make_num(ll_a)
b = make_num(ll_b)
print(a+b)
