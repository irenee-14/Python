'''
2025.8.29
6246 - 풍선 놀이
'''

n, q = map(int, input().split())
slot = [0] * (n + 1)
res = 0

for _ in range(q):
    l, i = map(int, input().split())
    for j in range(l, n + 1, i):
        slot[j] = 1

print(slot.count(0) - 1)

