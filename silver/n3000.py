'''
2024.2.19
3000 - 직각삼각형
'''

n = int(input())

points = []
cnt = 0

xCnt = [0 for _ in range(1000001)]
yCnt = [0 for _ in range(1000001)]

for i in range(n):
    x, y = map(int, input().split())
    xCnt[x] += 1
    yCnt[y] += 1
    points.append((x, y))

for i in range(n):
    x, y = points[i][0], points[i][1]
    cnt += (xCnt[x] - 1) * (yCnt[y] - 1)
print(cnt)
    
