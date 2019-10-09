
s = input().rstrip().split(' ')
H = int(s[0])
W = int(s[1])
N = int(s[2])
h = []
w = []
x = []

for i in range(N):
    s = input().rstrip().split(' ')
    h.append(int(s[0]))
    w.append(int(s[1]))
    x.append(int(s[2]))

field = [['.' for i in range(W)] for j in range(H)]

def fallable(h,w,x,row):
    for i in range(row):
        if(any([e == '#' for e in field[i][x:x+w]])):
            return False
    return True

def draw_field(h,w,x):
    hcount = 0
    for row in range(H-1, -1, -1):
        if(any([e == '#' for e in field[row][x:x+w]])):
            continue
        if(all([e == '.' for e in field[row][x:x+w]])):
            if(hcount == h):
                break
            if(fallable(h,w,x,row)):
                field[row][x:x+w] = ['#' for i in range(w)]
                hcount += 1
        

for i in range(N):
    draw_field(h[i],w[i],x[i])

for j in range(H):
    print("".join(field[j]))