H, W = map(int, input().split())
M = []
M.append(list(map(int, input().split())))
M.append(list(map(int, input().split())))
for i in range(2):
    diff = M[i][1] - M[i][0]
    for j in range(2, W):
        M[i].append(M[i][j-1] + diff)
row_diff = [M[1][j] - M[0][j] for j in range(W)]
for i in range(2, H):
    M.append([M[i-1][j] + row_diff[j] for j in range(W)])

for i in range(H):
    print(" ".join(map(str,M[i])))