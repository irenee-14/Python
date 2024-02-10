'''
2024.2.10
14940 - 쉬운 최단거리 (bfs)
'''
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
ground = []
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
visited = [[-1] * m for _ in range(n)]

for _ in range(n):
    ground.append(list(map(int, input().split())))

def bfs(i, j):
    que = deque()
    que.append([i, j])
    visited[i][j] = 0

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny <m and visited[nx][ny] == -1:
                if ground[nx][ny] == 0:
                    visited[nx][ny] = 0
                elif ground[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    que.append([nx, ny])

for i in range(n):
    for j in range(m):
        if ground[i][j] == 2 and visited[i][j] == -1:
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if ground[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()