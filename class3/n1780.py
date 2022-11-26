'''
2022.11.26
1780 - 종이의 개수
'''

import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

minus = 0
zero = 0
plus = 0


def dfs(x, y, n):
    global minus, zero, plus

    check = board[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if board[i][j] != check:
                for k in range(3):
                    for l in range(3):
                        dfs(x+k*n//3, y+l*n//3, n//3)
                return
    if check == -1:
        minus += 1
    elif check == 0:
        zero += 1
    else:
        plus += 1


dfs(0, 0, N)
print(f'{minus}\n{zero}\n{plus}')
