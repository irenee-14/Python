'''
2024.5.13 
4963 - 섬의 개수 (dfs)
'''
import sys
sys.setrecursionlimit(10000)

dx = [1, 1, -1, -1, 1, -1, 0, 0]
dy = [0, 1, 0, 1, -1, -1, 1, -1]

def dfs(x, y):
    board[x][y] = 0
    
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < h and 0 <= ny < w and board[nx][ny] == 1:
            dfs(nx, ny)

while True:
    w, h = map(int, input().split())
    
    if w == 0 and h == 0:
        break
    
    board = [list(map(int, input().split())) for _ in range(h)]
    
    count = 0
    
    for i in range(h):
        for j in range(w):
            if board[i][j] == 1:
                dfs(i, j)
                count += 1
    print(count)
