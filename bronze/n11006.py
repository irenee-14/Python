'''
2025.9.14
11006 - 남욱이의 닭장
'''

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    u = (m*2) - n
    t = n - m
    print(u, t)
