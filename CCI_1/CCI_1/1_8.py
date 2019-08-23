import random
N = 3
M = 4
X = [[random.randint(-10, 10) for j in range(N)] for i in range(M)]
Y = X.copy()

n = m = 2
for i in range(M):
    for j in range(N):
        if(i == n or j == m):
            Y[i][j] = 0
print(Y)


     