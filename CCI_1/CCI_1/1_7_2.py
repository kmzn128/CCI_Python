def rotate_matrix(M):
    N = len(M)
    MM = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            MM[i][j] = M[j][N-i-1]
    return MM

def main(n):
    M = [[i+j*10 for i in range(n)] for j in range(n)]
    print(M)
    print(rotate_matrix(M))
    
main(3)