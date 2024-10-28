'''
2024.10.28
2303 - 숫자 게임
'''
from itertools import combinations

n = int(input())
res = 0
res_max = 0

for i in range(n):
    nums = list(combinations(list(map(int, input().split())), 3))
    score = 0
    for num in nums:
        score = max(score, sum(num) % 10)
    if score >= res_max:
        res = i + 1
        res_max = score
print(res)

