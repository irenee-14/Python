'''
2024.4.8
2210 - 숫자판 점프
'''
res = []
board = []
for _ in range(5):
    board.append(list(map(str, input().split())))
    
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def dfs(x, y, num):
    if len(num) == 6:
        res.append(num)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, num + board[nx][ny])


for i in range(5):
    for j in range(5):
        dfs(i, j, board[i][j])
print(len(set(res)))
