input = [15,16,19,20,25,1,3,4,5,7,10,14]

def search_rot_point(_input):
    for i in range(len(_input)-1):
        if(_input[i] > _input[i+1]):
            return i + 1

def binary_search(_list, elem, low, high):
    if (low > high):
        return -1 # error
    mid = low + (high - low)//2
    if(elem < _list[mid]):
        return binary_search(_list, elem, low, mid-1)
    elif(elem > _list[mid]):
        return binary_search(_list, elem, mid+1, high)
    else:
        return mid

cut = search_rot_point(input)
new_input = input[cut:] + input[:cut]
print(cut + binary_search(new_input, 5, 0, len(input)-1))
