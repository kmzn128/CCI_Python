import random
ll = sorted([random.randint(0,200) for i in range(63)])
minus = [-1 for i in range(200)]
target_ind = random.randint(1,63)

listlike = ll + minus

target_val = listlike[target_ind]

def gen_exp_2():
    i = 0
    while(True):
        yield 2**i
        i += 1

def find_elem(listy, target_val, left, right):
    if(left > right):
        return None
    mid = left + (right-left)//2
    if(listy[mid] > target_val or listy[mid] == -1):
        return find_elem(listy, target_val, left, mid-1)
    elif(listy[mid] < target_val):
        return find_elem(listy, target_val, mid+1, right)
    else:
        return mid, target_val

def find_elem_with_minus(listy, target_val, left, right):
    pass

def find_elem_in_listlike(listy, target_val):
    i = 0
    gen = gen_exp_2()
    while(True):
        if(listy[i] == target_val):
            return i, target_val
        elif(listy[i] > target_val or listy[i] == -1):
            return find_elem(listy, target_val, i//2, i)
        elif(listy[i] < target_val):
            i = next(gen)
            continue
        else:
            pass
        

print(find_elem_in_listlike(listlike, target_val))


