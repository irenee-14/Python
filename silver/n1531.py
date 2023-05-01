'''
2023.5.1
1531 - 투명
'''
n, m = map(int, input().split())
board = [[0] * 101 for _ in range(101)]

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            board[i][j] += 1 
res = 0 
for i in range(101):
    for j in range(101):
        if board[i][j] > m:
            res += 1
print(res)
    
