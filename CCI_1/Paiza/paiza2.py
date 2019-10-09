# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
import heapq
import math

s = input().rstrip().split(' ')
M = int(s[0])
N = int(s[1])
buf = []
start = None
goal = None
for i in range(N):
    s = input().rstrip().split(' ')
    row = []
    for j in range(M):
        row.append(str(s[j]))
        if(str(s[j]) == 's'):
            start = (i,j)
        if(str(s[j]) == 'g'):
            goal = (i,j)
    buf.append(row)

dirs = [(0,1),(0,-1),(1,0),(-1,0)]

def get_next(i,j):
    nexts = []
    for n_i, n_j in dirs:
        if(i+n_i >= 0 and i+n_i < N and j+n_j >= 0 and j+n_j < M):
            if(buf[i+n_i][j+n_j] == '0' or buf[i+n_i][j+n_j] == 'g'):
                nexts.append((i+n_i, j+n_j))
    return nexts

def calc_distance_togoal(i,j):
    return math.sqrt((i - goal[0])**2+(j-goal[1])**2)
        

    
def calc_distance(s,g):
    path = [s]
    hpq = []
    cost = len(path) + calc_distance_togoal(s[0],s[1])
    visited = {start:cost}
    heapq.heappush(hpq, (cost, path))
    while(len(hpq) > 0):
        cost, path = heapq.heappop(hpq)
        latest_pos = new_path[-1]
        if(latest_pos == g):
            return new_cost
        nexts = get_next(latest_pos)
        for n in nexts:
            new_path = path + [n]
            new_cost = cost + calc_distance_togoal(n[0],n[1])
            if(n in visited and new_cost >= visited[n]):
                continue
            else:
                visited[n] = new_cost
                heapq.heappush(hpq, (new_cost, new_path))

print(calc_distance(start,goal))
    
