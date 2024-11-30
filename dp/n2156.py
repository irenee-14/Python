'''
2024.11.30
2156 - 포도주 시식
'''

import sys
sys.setrecursionlimit(9999999)
def recur(idx):
    if dp[idx] == -1:
        dp[idx] = max(
            recur(idx - 1),  # idx를 마시지 않는 경우
            recur(idx - 2) + grape[idx - 1],  # idx를 마시고 idx-1은 마시지 않는 경우
            recur(idx - 3) + grape[idx - 1] + grape[idx - 2]  # idx와 idx-1을 마시고 idx-2는 마시지 않는 경우
        )
    return dp[idx]

n = int(input())
grape = [int(input()) for _ in range(n)]
dp = [-1 for _ in range(n + 1)]

dp[0] = 0
if n > 0:
    dp[1] = grape[0]
if n > 1:
    dp[2] = grape[0] + grape[1]

print(recur(n))
