'''
2022.11.12
1012 - 유기농 배추
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x, y):
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx and nx < M) and (0 <= ny and ny< N):
            if field[ny][nx] == 1:
                field[ny][nx] = 0 
                dfs(nx, ny)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0]*M for row in range(N)]
    cnt = 0
    
    for i in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1
    
    for i in range(M):
        for j in range(N):
            if field[j][i] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)
    
