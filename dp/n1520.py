'''
2024.12.11
1520 - 내리막 길
'''

import sys
sys.setrecursionlimit(999999999)

# 왼쪽 위에서 오른쪽 아래로 이동 가능한 경로의 수
def recur(y, x):
    if y == Y - 1 and x == X - 1:
        return 1

    if dp[y][x] != -1: # 모든 지점에서 계산이 한번이라도 된다면 재사용!
        return dp[y][x]

    route = 0
    for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ey = y + dy
        ex = x + dx
        if 0 <= ey < Y and 0 <= ex < X:
            if graph[y][x] > graph[ey][ex]:  # 이동 가능
                route += recur(ey, ex)
    dp[y][x] = route
    return route


Y, X = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(Y)]
dp = [[-1 for _ in range(X)] for _ in range(Y)]

res = recur(0, 0)
print(res)
