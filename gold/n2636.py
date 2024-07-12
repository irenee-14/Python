'''
2024.5.29 
2636 - 치즈(bfs)
'''
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    que = deque()
    que.append((0, 0))
    visited[0][0] = True
    cnt = 0
    
    while que:
        x, y = que.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                visited[nx][ny] = True
                
                if board[nx][ny]:
                    board[nx][ny] = 0
                    cnt += 1
                else:
                    que.append((nx, ny))
    history.append(cnt)
    return cnt

h, w = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)]

history = []
time = 0

while True:
    visited = [[False] * w for _ in range(h)]

    melt = bfs()

    if melt == 0:
        print(time)
        print(history[-2])
        break
    time += 1   
