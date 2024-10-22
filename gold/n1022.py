'''
2024.10.22
1022 - 소용돌이 예쁘게 출력하기
'''

r1, c1, r2, c2 = map(int, input().split())

board = [[0] * (c2 - c1 + 1) for _ in range(r2 - r1 + 1)]
m = 0

def cal(r, c):
    bor = max(abs(r), abs(c))
    level = (bor * 2 - 1) ** 2 + 1

    if r == bor:
        return level + bor * 7 + c - 1
    if c == -bor:
        return level + bor * 5 + r - 1
    if r == -bor:
        return level + bor * 3 - c - 1

    return level + bor - r - 1


for i in range(r1, r2 + 1):
    for j in range(c1, c2 + 1):
        board[i - r1][j - c1] = cal(i, j)
        m = max(m, board[i - r1][j - c1])

for i in range(r2 - r1 + 1):
    for j in range(c2 - c1 + 1):
        print(str(board[i][j]).rjust(len(str(m))), end=' ')
    print()