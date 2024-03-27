'''
2024.3.27
1913 - 달팽이
'''
n = int(input())
num = int(input())

board = [[1] * n for _ in range(n)]

# 오른쪽, 아래, 왼쪽, 위
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = n // 2, n // 2
index = 1
part = 0
res = [x + 1, y + 1]

while True:
    for i in range(4):
        for _ in range(part):
            x += dx[i]
            y += dy[i]
            index += 1 
            board[x][y] = index 
            if index == num:
                res = [x + 1, y + 1]
    
    if x == y == 0:
        break 
    x -= 1 
    y -= 1 
    part += 2
    
    
for i in range(n):
    print(*board[i])
print(*res)
    
