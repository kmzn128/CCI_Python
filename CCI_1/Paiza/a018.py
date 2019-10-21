import math

W, H, M, N = map(int, input().split())
cams = []
for i in range(M):
    cams.append(list(map(int, input().split())))
objs = []
for i in range(N):
    objs.append(list(map(int, input().split())))

def euclid_distance(x, y, a, b):
    return math.sqrt((x-a)**2+(y-b)**2)
    
def reachable(x, y, a, b, r):
    return r - euclid_distance(x, y, a, b) > 0

def in_angle(x, y, a, b, t, d):
    t_deg = math.atan2(b-y, a-x) * 180 / math.pi 
    if(t_deg < 0):
        t_deg += 360
    low_bound_deg = t - d/2
    upper_bound_deg = t + d/2
    return t_deg >= low_bound_deg and t_deg <= upper_bound_deg

def judge_oservable(a,b):
    for i in range(M):
        if(reachable(cams[i][0], cams[i][1], a, b, cams[i][4])):
            if(in_angle(cams[i][0], cams[i][1], a, b, cams[i][2], cams[i][3])):
                return "yes"
    return "no"
    
for i in range(N):
    print(judge_oservable(objs[i][0], objs[i][1]))

