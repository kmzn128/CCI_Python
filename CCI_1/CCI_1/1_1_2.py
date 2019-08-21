str_list = list("jjfweoaifjao")
import string

dict_alphabet = {c:False for c in string.ascii_lowercase}
new_str_list = []

for ch in str_list:
    if(dict_alphabet[ch]):
        continue
    else:
        dict_alphabet[ch] = True
        new_str_list.append(ch)
print(new_str_list)