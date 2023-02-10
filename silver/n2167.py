'''
2022.1.5
2167 - 2차원 배열의 합
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
res = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n):
    arr.append(list(map(int, input().split())))
for i in range(1, n + 1):
    for j in range(1, m + 1):
        res[i][j] = arr[i - 1][j - 1] + res[i][j - 1] + res[i - 1][j] - res[i - 1][j - 1]

k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(res[x][y] - res[x][j - 1] - res[i - 1][y] + res[i - 1][j - 1])
    
        
