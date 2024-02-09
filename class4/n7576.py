'''
2024.2.9
7576 - 토마토 (bfs)
'''
import sys
input = sys.stdin.readline
from collections import deque

M, N = map(int, input().split())
box = []
que = deque([])
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

for i in range(N):
    box.append(list(map(int, input().split())))
    for j in range(M):
        if box[i][j] == 1:
            que.append([i, j])

while que:
    x, y = que.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                que.append([nx, ny])

res = 0
for line in box:
    for to in line:
        if to == 0:
            print(-1)
            exit()
    res = max(res, max(line))

print(res - 1)