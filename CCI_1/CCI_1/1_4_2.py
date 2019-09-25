def remove_space(str_in):
    li = []
    for c in str_in:
        if c != " ":
            li.append(c)
    st = ""
    return st.join(li)
            
def lower(str_in):
    return str_in.lower()

def sort(str_in):
    return sorted(str_in)

def check_palindrome(str_in):
    str_in = remove_space(str_in)
    str_in = lower(str_in)
    str_in = sort(str_in)
    only_one_word_counter = 0
    li = list(str_in)
    set_li = set(li)
    for c in set_li:
        if(li.count(c) % 2 == 0):
            continue
        elif(li.count(c) % 2 == 1):
            only_one_word_counter += 1
        else:
            pass # can't happen
    return  only_one_word_counter <= 1 
            


str_in = "Tact Coat"
print(check_palindrome(str_in))