str_list = list("jjfweoaifjao")

new_str_list = []

def check_dups(_char, _str):
    for elem in _str:
        if elem == _char:
            return True
    return False

for c in str_list:
    if len(new_str_list) == 0:
        new_str_list.append(c)
        continue
    if(check_dups(c, new_str_list)):
        continue
    else:
        new_str_list.append(c)

        
print(str(new_str_list))



