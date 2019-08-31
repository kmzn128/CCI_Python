str_a = "abcdef"
str_b = "cdefaa"

list_a = list(str_a)
list_b = list(str_b)

int_list_a = [ord(x) for x in list_a]
int_list_b = [ord(y) for y in list_b]

def sort_function(_list):
    for i in range(len(_list)):
        min_index = i
        for j in range(i+1, len(_list)):
            if(_list[min_index] > _list[j]):
                min_index = j
        _list[min_index], _list[i] = _list[i], _list[min_index]
    return _list


sorted_a = sort_function(int_list_a)
sorted_b = sort_function(int_list_b)

print(sorted_a)
print(sorted_b)