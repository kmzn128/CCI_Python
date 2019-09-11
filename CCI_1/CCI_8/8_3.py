
A = [-100, -51, -32, -7, -1, 3, 7, 16, 44, 60]

def find_magic_index(_list, right, left):
    if (right > left):
        return
    mid = right + (left - right) // 2
    if(A[mid] < mid):
        return find_magic_index(_list, mid+1, left)
    elif(A[mid] > mid):
        return find_magic_index(_list, right, mid-1)
    elif(A[mid] == mid):
        return A[mid]
    else:
        return

print(find_magic_index(A, 0, len(A)-1))