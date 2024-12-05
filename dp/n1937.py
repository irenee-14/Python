'''
2024.12.5
1937 - 많이 이동하기(욕심쟁이 판다)
'''

import sys
sys.setrecursionlimit(999999999)
def recur(y, x):

    if dp[y][x] != 0:
        return dp[y][x]

    for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ey = y + dy
        ex = x + dx

        if 0 <= ey < n and 0 <= ex < n:
            if graph[y][x] < graph[ey][ex]: # 이동 가능
                dp[y][x] = max(dp[y][x], recur(ey, ex) + 1)
        # max(recur(y - 1, x),  recur(y + 1, x), recur(y, x - 1), recur(y, x + 1))
    return dp[y][x]


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 모든 경우의 수를 탐색 한 후 dp로 변경
# 1. 모든 점을 방문한다
# 2. 방문한 뒤에 이동할 수 있는 모든 경우의 수를 재귀로 구현한다
# 3. 재귀로 구현한 뒤 DP로 바꾼다!

dp = [[0 for _ in range(n)] for _ in range(n)]

for y in range(n):
    for x in range(n):
        recur(y, x)

print(max(map(max, dp)) + 1)