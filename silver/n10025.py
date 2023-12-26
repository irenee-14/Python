'''
2023.12.26
10025 - 게으른 백곰
'''
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
cage = [0] * 1000001
end = 0 

for _ in range(n):
    g, x = map(int, input().split())
    cage[x] = g 
    end = max(end, x)

size = 2 * k + 1

window = sum(cage[:size])
res = window

for i in range(size, end):
    window += cage[i] - cage[i - size]
    res = max(res, window)
print(res)

