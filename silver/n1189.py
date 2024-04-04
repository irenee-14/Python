'''
2024.4.4 
1189 - 컴백홈(dfs)
'''
R, C, K = map(int, input().split())
board = []
for i in range(R):
    board.append(list(input()))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

res = 0

def dfs(x, y, cnt):
    global res 
    
    if cnt == K and x == 0 and y == C - 1:
        res += 1 
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        if 0 <= nx < R and 0 <= ny < C and board[nx][ny] == '.':
            board[nx][ny] = 'T'
            dfs(nx, ny, cnt + 1)
            board[nx][ny] = '.'
            
board[R - 1][0] = 'T'
dfs(R - 1, 0, 1)
print(res)
    
