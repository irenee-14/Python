'''
2024.3.2
2740 - 행렬 곱셈
'''
A = []
B = []

N, M = map(int, input().split())
for i in range(N):
    A.append(list(map(int, input().split())))

M, K = map(int, input().split())
for i in range(M):
    B.append(list(map(int, input().split())))

C = [[0 for _ in range(K)] for _ in range(N)]

for n in range(N):
    for k in range(K):
        for m in range(M):
            C[n][k] += A[n][m] * B[m][k]
for i in range(len(C)):
    print(*C[i], sep=' ')