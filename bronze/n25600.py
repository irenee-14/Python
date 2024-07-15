'''
2024.7.15
25600 - Triathlon
'''

res = 0
n = int(input())
for _ in range(n):
    a, d, g = map(int, input().split())
    if a == d + g:
        value = a * (d + g) * 2
    else:
        value = a * (d + g)
    res = max(value, res)

print(res)