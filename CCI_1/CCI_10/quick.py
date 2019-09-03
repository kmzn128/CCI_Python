import random

li = [random.randint(0,100) for x in range(10)]

print(li)

def quick_sort(_list, left, right):
    if( left < right ):
        i = left
        j = right
        pivot = _list[i+(j-i)//2]
        while(True):
            while(_list[i] < pivot):
                i += 1
            while(_list[j] > pivot):
                j -= 1
            if(i >= j):
                break
            _list[i], _list[j] = _list[j], _list[i]
            i += 1
            j -= 1
        quick_sort(_list, left, i-1)
        quick_sort(_list, j+1, right)

quick_sort(li, 0, len(li)-1)
print(li)

