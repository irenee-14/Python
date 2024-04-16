'''
2024.4.16 
7562 - 나이트의 이동
'''
from collections import deque

#  (1, -2) (2, -1) (2, 1) (1, 2) (-1, 2) (-2, 1) (-2, -1) (-1, -2)
def bfs():
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]
    q = deque()
    q.append((startX, startY))
    
    while q:
        x, y = q.popleft()
        
        if x == endX and y == endY:
            return visited[x][y]
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < l and 0 <= ny < l and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1 
                q.append((nx, ny))

N = int(input())

for _ in range(N):
    l = int(input())
    startX, startY = map(int, input().split())
    endX, endY = map(int, input().split())
    
    
    visited = [[0] * l for _ in range(l)]
    visited[startX][startY] = 1 
    print(bfs() - 1)
