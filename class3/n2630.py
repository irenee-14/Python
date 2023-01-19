'''
2023.1.19
2630 - 색종이 만들기
'''

# 시작점
# (x, y)        (x, y + n/2)
# (x + n/2, y)  (x + n/2, y + n/2)

import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
res = []

def make(x, y, n):
    color = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != paper[i][j]:
                make(x, y, n//2)
                make(x, y + n//2, n//2)
                make(x + n//2, y, n//2)
                make(x + n//2, y + n//2, n//2)
                return
    if color == 0:
        res.append(0)
    else:
        res.append(1)

make(0, 0, n)
print(res.count(0))
print(res.count(1))