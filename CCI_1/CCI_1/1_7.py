import random
N = 3
M = [[j*(i+1) for j in range(N)] for i in range(N)]

X = [[0 for j in range(N)] for i in range(N)]
for i in range(N):
    for j in range(N):
        X[N-1-j][i] = M[i][j]
print(X)