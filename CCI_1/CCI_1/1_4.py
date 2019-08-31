st = "Tact Coa"

def lower(_str):
    _list = []
    str_list = list(_str)
    for c in str_list:
        if(c.isalnum()):
            _list.append(c.lower())
    return _list

def sort(_list):
    _list = [ord(x) for x in _list]
    for i in range(len(_list)):
        min_index = i
        for j in range(i+1, len(_list)):
            if(_list[min_index] > _list[j]):
                min_index = j
        _list[i], _list[min_index] = _list[min_index], _list[i]
    return _list

def check_palindrome(_list):
    pass

list_lowered = lower(st)
list_sorted = sort(list_lowered)
print(check_palindrome(list_sorted))