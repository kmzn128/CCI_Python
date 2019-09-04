from linked_list import LinkedList

ll = LinkedList()

input_list = [3,5,8,5,10,2,1]

for i in input_list:
    ll.appendToTail(i)

pivot_node = ll.find(5)
before_runner = ll.head
after_runner = pivot_node

while(before_runner is not pivot_node):
    if(before_runner.data > pivot_node.data):
        value = before_runner.data
        ll.remove_by_node(before_runner)
        ll.insert(value, pivot_node)
    before_runner = before_runner.next

while(after_runner):
    if(after_runner.data < pivot_node.data):
        value = after_runner.data
        ll.remove_by_node(after_runner)
        ll.insert(value, ll.head)
    after_runner = after_runner.next

ll.list_print()