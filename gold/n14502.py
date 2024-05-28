'''
2024.5.28 
14502 - 연구소 (bfs)
'''
from collections import deque
import copy

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    que = deque()
    tmp = copy.deepcopy(board)
    
    for i in range(N):
        for j in range(M):
           if tmp[i][j] == 2:
               que.append((i, j))
    while que:
        x, y = que.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                que.append((nx, ny))

            
    global res 
    safe = 0
    
    for i in range(N):
        safe += tmp[i].count(0)
    res = max(safe, res)


def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                board[i][j] = 1
                wall(cnt + 1)
                board[i][j] = 0
    

N, M = map(int, input().split())
board = [list(map(int, input().split())) for i in range(N)]

res = 0
wall(0)
print(res)

