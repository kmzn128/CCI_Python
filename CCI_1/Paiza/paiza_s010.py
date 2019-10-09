il = input().rstrip().split(' ')
T = int(il[0])
B = int(il[1])
U = int(il[2])
D = int(il[3])
L = int(il[4])
R = int(il[5])
N = int(input())
p = []
for i in range(N):
    p.append(int(input()))

def make_dic(T,B,U,D,L,R):
    dic = {}
    dic.update({T:{T:0,L:1,U:1,R:1,D:1,B:2}})
    dic.update({L:{T:1,L:0,U:1,R:2,D:1,B:1}})
    dic.update({U:{T:1,L:1,U:0,R:1,D:2,B:1}})
    dic.update({R:{T:1,L:2,U:1,R:0,D:1,B:1}})
    dic.update({D:{T:1,L:1,U:2,R:1,D:0,B:1}})
    dic.update({B:{T:2,L:1,U:1,R:1,D:1,B:0}})
    return dic

dic = make_dic(T,B,U,D,L,R)
sum = 0
for i in range(N-1):
    sum += dic[p[i]][p[i+1]]
    
print(sum)