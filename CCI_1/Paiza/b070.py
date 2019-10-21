

s = input().split(' ')
N = int(s[0])
M = int(s[1])
w = []
for i in range(N):
    w.append(int(input()))
target = M // 2
w.sort()
def trim_upper(li, thres):
    out_li = []
    for e in li:
        if(e <= thres):
            out_li.append(e)
        else:
            break
    return out_li
trim_w = trim_upper(w, target)
from itertools import chain, combinations
def powerset(li):
    return chain.from_iterable(combinations(li, i) for i in range(len(li)+1))
def find_candidates(li, target):
    power = powerset(li)
    sum_power = [sum(e) for e in power]
    sum_power.sort()
    trim_power = trim_upper(sum_power, target)
    for i in range(target, 0, -1):
        if trim_power.count(i) >= 2:
            return i*2
    return 0
print(find_candidates(trim_w, target))
        
    

    