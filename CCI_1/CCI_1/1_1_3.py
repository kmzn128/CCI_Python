st = "abcde"

def check_str(_str):
    li = list(_str)
    for i in range(len(li)-1):
        for j in range(i+1, len(li)):
            if li[i] == li[j]:
                return False
    return True

print(check_str(st))