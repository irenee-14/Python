'''
2025.3.10
5568 - 카드 놓기
'''

from itertools import permutations

n, k = int(input()), int(input())
nums = []
result = set()
for i in range(n):
    num = input()
    nums.append(num)

for per in permutations(nums, k):
    result.add(''.join(per))

print(len(result))