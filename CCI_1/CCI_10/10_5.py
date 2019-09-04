input = ["","","aaa","","","","","bbb","","","",""]

def sparse_search(_li, item, low, high):
    if(low > high):
        return -1
    mid = low + (high - low)//2
    while(_li[mid] == "" and mid < high):
        mid += 1
    if(_li[mid] == "" or _li[mid] > item):
        return sparse_search(_li, item, low, mid-1)
    elif(_li[mid] < item):
        return sparse_search(_li, item, mid+1, high)
    else:
        return mid

#print(sparse_search(input, "abc", 0, len(input)-1))
print(sparse_search(input, "bbb", 0, len(input)-1))