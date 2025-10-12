'''
2025.10.12
21212 - Cakes
'''


n = int(input())
res = []
for _ in range(n):
    a, b = map(int, input().split())
    res.append(b // a)
print(min(res))