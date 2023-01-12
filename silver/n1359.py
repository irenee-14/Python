'''
2023.1.12
1359 - 복권
'''
from itertools import combinations

n, m, k = map(int, input().split())

comb = list(combinations([i for i in range(n)], m))
res = 0 
for i in comb:
    cnt = 0
    for j in range(m):
        if i[j] < m:
            cnt += 1
    if cnt >= k:
        res += 1

print(res / len(comb))
