li = [None for x in range(30)]

print(li)
top_a = 0
top_b = 1
top_c = 2

def push_a(item):
    global top_a
    li[top_a] = item
    top_a += 3

def push_b(item):
    global top_b
    li[top_b] = item
    top_b += 3

def push_c(item):
    global top_c
    li[top_c] = item
    top_c += 3

def pop_a():
    global top_a
    if(top_a != 0):
        top_a -= 3
        ret = li[top_a]
        li[top_a] = None
        return ret

def pop_b():
    global top_b
    if(top_a != 1):
        top_b -= 3
        ret = li[top_b]
        li[top_b] = None
        return ret

def pop_c():
    global top_c
    if(top_a != 2):
        top_c -= 3
        ret = li[top_c]
        li[top_c] = None
        return ret

push_a(1)
push_a(2)
push_b(3)
push_c(4)
pop_a()
print(li)
