'''
2024.2.6
11049 - 행렬 곱셈 순서 (행렬 체인 곱셈, dp), pypy
'''

import sys
input = sys.stdin.readline

N = int(input())

board = []
dp = [[0] * N for _ in range(N)]

board = list(map(int, input().split()))
for _ in range(N - 1):
    r, c = map(int, input().split())
    board.append(c)

# (1,1) (2,2) (1,2) (3,3) (2,3) (1,3) ... (2,5) (1,5)
# 왼쪽부터 오른쪽, 아래에서 위 방향
for d in range(N):
    for i in range(N - d):
        j = i + d
        if i == j:
            continue

        dp[i][j] = float('inf')
        for k in range(i, j):
            dp[i][j] = min(dp[i][j],
                           dp[i][k] + dp[k + 1][j]
                           + board[i] * board[k + 1] * board[j + 1])

print(dp[0][-1])