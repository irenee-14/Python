'''
2025.10.18
9848 - Gift
'''

n, k = map(int, input().split())
li = [int(input()) for _ in range(n)]
res = 0

for i in range(n - 1):
    if li[i] - li[i + 1] >= k:
        res += 1
print(res)
