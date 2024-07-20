'''
2024.7.20
2460 - 지능형 기차 2
'''

res = 0
total = 0

for i in range(10):
    a, b = map(int, input().split())
    total -= a
    total += b
    res = max(res, total)
print(res)