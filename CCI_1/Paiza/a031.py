
input_line = input().split(' ')
p = list(map(int, input_line[:3]))
k = int(input_line[3])
index = 2
produced = 2

def factorizable(p, produced):
    while(True):
        if(produced % p[0] == 0):
            produced //= p[0]
            if(produced == 1):
                return True
            continue
        if(produced % p[1] == 0):
            produced //= p[1]
            if(produced == 1):
                return True
            continue
        if(produced % p[2] == 0):
            produced //= p[2]
            if(produced == 1):
                return True
            continue
        return False

while(True):
    if(factorizable(p, produced)):
        index += 1
        if(index > k):
            break
    produced += 1
    
if(k == 1):
    print(1)
else:
    print(produced)