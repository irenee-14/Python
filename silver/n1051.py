'''
2024.5.30
1051 - 숫자 정사각형 
'''
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

res = 1

for k in range(min(N, M), 0, -1):
    for i in range(N - k):
        for j in range(M - k):
            if board[i][j] == board[i][j + k] == board[i + k][j] == board[i + k][j + k]:
                    res = max(res, (k + 1) ** 2)
print(res)
