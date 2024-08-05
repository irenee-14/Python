'''
2024.8.5
1388 - 바닥 장식
'''

n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(input()))

cnt = 0
for i in range(n):
    tmp = ''
    for j in range(m):
        if board[i][j] == '-':
            if board[i][j] != tmp:
                cnt += 1
        tmp = board[i][j]
for j in range(m):
    tmp = ''
    for i in range(n):
        if board[i][j] == '|':
            if board[i][j] != tmp:
                cnt += 1
        tmp = board[i][j]
print(cnt)