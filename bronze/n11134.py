'''
2025.7.3
11134 - 쿠키애호가
'''

t = int(input())

for _ in range(t):
    res = 0
    n, c = map(int, input().split())
    res = n // c
    if n % c > 0:
        res += 1
    print(res)

