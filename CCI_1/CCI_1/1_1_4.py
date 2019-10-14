
STR = "abcdea"

def check(str):
    check_set = set()
    for c in STR:
        if c in check_set:
            return False
        else:
            check_set.add(c)
    return True
        
print(check(STR))   