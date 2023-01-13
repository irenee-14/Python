'''
2023.1.13
4307 - 개미
'''

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    l, n = map(int, input().split())
    nums = []
    for _ in range(n):
        nums.append(int(input()))
    nums.sort()
    min_time = 0
    max_time = 0

    for ant in nums:
        min_time = max(min_time, min(ant, l - ant))
        max_time = max(max_time, ant, l - ant)
    print(min_time, max_time)
