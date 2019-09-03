import random

li_A = sorted([random.randint(0,100) for x in range(5)])
li_B = sorted([random.randint(0,100) for x in range(5)])

print(li_A)
print(li_B)

def _insert(_li, elem):
    for i in range(len(_li)):
        if(_li[i] > elem):
            _li.insert(i, elem)
            break

def inserting(l_a, l_b):
    for elem in l_b:
        _insert(l_a, elem)

inserting(li_A, li_B)
print(li_A)


