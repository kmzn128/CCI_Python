def _insert(li, el, l, r):
    if(r-l < 0):
        return
    if(r-l == 0):
        if(li[l] > el):
            li.insert(l,el)
        else:
            #if(l == len(li)):
            #   li.append(el)
            #else:
            li.insert(l+1, el)
    mid = l + (r-l)//2
    if(el < li[mid]):
        _insert(li,el,l,mid-1)
    else:
        _insert(li,el,mid+1,r)
        
def insert_another_array(a, b):
    left = 0
    for elem_b in b:
        right = len(a)-1
        _insert(a, elem_b, left, right)

a = [2,4,8,14,26,35,46,78,90,100]
b = [23,34,45,56,67,200]

insert_another_array(a, b)
print(a)