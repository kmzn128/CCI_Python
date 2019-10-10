# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

s = input().split(" ")
H = int(s[0])
W = int(s[1])

wall = []
for i in range(H):
    wall.append(list(input()))

pos = [0,0]
prev = [0,-1]
num_path = 0

def check_prev(pos, prev):
    if(pos[0]-prev[0] == 1):
        return 'u'
    elif(prev[0]-pos[0] == 1):
        return 'd'
    elif(pos[1]-prev[1] == 1):
        return 'l'
    elif(prev[1]-pos[1] == 1):
        return 'r'

def go_next(di):
    if(di == 'u'):
        return [pos[0]-1, pos[1]]
    elif(di == 'd'):
        return [pos[0]+1, pos[1]]
    elif(di == 'l'):
        return [pos[0], pos[1]-1]
    elif(di == 'r'):
        return [pos[0], pos[1]+1]

def get_next(pos, prev):
    if(wall[pos[0]][pos[1]] == '_' ):
        if(check_prev(pos, prev) == 'u'):
            return go_next('d'), pos
        elif(check_prev(pos, prev) == 'd'):
            return go_next('u'), pos
        elif(check_prev(pos, prev) == 'l'):
            return go_next('r'), pos
        elif(check_prev(pos, prev) == 'r'):
            return go_next('l'), pos
    elif(wall[pos[0]][pos[1]] == '/'):
        if(check_prev(pos, prev) == 'u'):
            return go_next('l'), pos
        elif(check_prev(pos, prev) == 'd'):
            return go_next('r'), pos
        elif(check_prev(pos, prev) == 'l'):
            return go_next('u'), pos
        elif(check_prev(pos, prev) == 'r'):
            return go_next('d'), pos
    else:
        if(check_prev(pos, prev) == 'u'):
            return go_next('r'), pos
        elif(check_prev(pos, prev) == 'd'):
            return go_next('l'), pos
        elif(check_prev(pos, prev) == 'l'):
            return go_next('d'), pos
        elif(check_prev(pos, prev) == 'r'):
            return go_next('u'), pos

while(pos[0] >= 0 and pos[1] >= 0 and pos[1] < W and pos[0] < H):
    pos, prev = get_next(pos, prev)
    num_path += 1
print(num_path)