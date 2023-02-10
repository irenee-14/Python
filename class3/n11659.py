'''
2023.1.10
11659 - 구간 합 구하기4
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
sum = [0]

tmp = 0 
for i in nums:
    tmp += i
    sum.append(tmp)

for _ in range(m):
    i, j = map(int, input().split())
    print(sum[j] - sum[i-1])
