'''
2025.2.3
17466 - N! mod P (1)
'''

n, p = map(int, input().split())
res = 1
for i in range(2, n + 1):
    res = (res * i) % p
print(res % p)