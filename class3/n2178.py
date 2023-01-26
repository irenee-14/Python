'''
2023.1.25
2178 - 미로 탐색
'''

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

miro = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    que = deque([])
    que.append((x, y, 1))
    visited[x][y] = 1

    while que:
        x, y, distance = que.popleft()

        if x == n - 1 and y == m - 1:
            print(distance)
            break
        else:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and miro[nx][ny] == 1:
                    visited[nx][ny] = 1
                    que.append((nx, ny, distance + 1))


bfs(0, 0)
