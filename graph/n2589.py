'''
2024.12.24
2589 - 보물섬
'''

# from collections import deque
#
# Y, X = map(int, input().split())
# graph = [list(input().rstrip()) for _ in range(Y)]
#
# maxi = 0
#
# for y in range(Y):
#     for x in range(X):
#         if graph[y][x] == 'L':
#             # 좌표가 변할떄마다 초기화
#             visited = [[0 for _ in range(X)] for _ in range(Y)]
#             dist = [[0 for _ in range(X)] for _ in range(Y)]
#
#              # BFS
#             q = deque()
#             q.append([y, x])
#             visited[y][x] = 1
#
#             while q:
#                 ey, ex = q.popleft()
#
#                 # 4방향 탐색 2차원 DP
#                 for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#                     ny, nx = ey + dy, ex + dx
#                     if 0 <= ny < Y and 0 <= nx < X:
#                         if graph[ny][nx] == 'L':
#                             if visited[ny][nx] == 0:
#                                 visited[ny][nx] = 1
#                                 dist[ny][nx] = dist[ey][ex] + 1
#                                 maxi = max(maxi, dist[ny][nx])
#                                 q.append([ny, nx])
# print(maxi)


from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q.append([x, y])
    c = [[0]*m for _ in range(n)]
    c[x][y] = 1
    num = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] == 'L' and c[nx][ny] == 0:
                    c[nx][ny] = c[x][y] + 1
                    num = max(num, c[nx][ny])
                    q.append([nx, ny])
    return num-1

n, m = map(int, input().split())
a = [list(map(str, input())) for _ in range(n)]
q = deque()

cnt = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == 'L':
            cnt = max(cnt, bfs(i, j))
print(cnt)

