'''
2025.3.29
30802 - 웰컴 키트
'''
import math


n = int(input())
sizes = map(int, input().split())
t, p = map(int, input().split())

res = 0

for size in sizes:
    if size > 0:
        res += math.ceil(size / t)

print(res)
print(n // p, n % p)
