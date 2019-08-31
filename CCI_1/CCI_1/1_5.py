str_a = "pale"
str_b = "ple"
str_c = "pales"
str_d = "bale"
str_e = "bake"

def compare_strings(s_a, s_b):
    s_a = list(s_a)
    s_b = list(s_b)
    strlen_dif = abs(len(s_a) - len(s_b))
    if( strlen_dif > 1):
        return False
    elif( strlen_dif == 1):
        for c_a, c_b in zip(s_a, s_b):
            if(c_a != c_b):
                if(len(s_a) > len(s_b)):
                    s_a.remove(c_a)
                    break
                else:
                    s_b.remove(c_b)
                    break
        if(len(s_a) > len(s_b) ):
            s_a.remove(s_a[-1])
        elif(len(s_a) < len(s_b)):
            s_b.remove(s_b[-1])
        return s_a == s_b
    else:
        b_once = False
        for c_a, c_b in zip(s_a, s_b):
            if(c_a != c_b):
                if(not b_once):
                    b_once = True
                    continue
                else:
                    return False
        return True


         



print(compare_strings(str_a, str_b))
print(compare_strings(str_a, str_c))
print(compare_strings(str_a, str_d))
print(compare_strings(str_a, str_e))

