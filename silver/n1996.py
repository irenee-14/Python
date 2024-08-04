'''
2024.8.4
1996 - 지뢰 찾기
'''

n = int(input())
board = []
dir = [(-1, 0), (-1, 1), (0, 1), (1, 1),
       (1, 0), (1, -1), (0, -1), (-1, -1)]

for i in range(n):
    board.append(list(input()))


res = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if board[i][j] != '.':
            tmp = int(board[i][j])
            for dx, dy in dir:
                if 0 <= i + dx < n and 0 <= j + dy < n:
                    res[i + dx][j + dy] += tmp

for i in range(n):
    for j in range(n):
        if board[i][j] != '.':
            print('*', end='')
        elif res[i][j] >= 10:
            print('M', end='')
        else:
            print(res[i][j], end='')
    print()
