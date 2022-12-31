'''
2022.12.31
11286 - 절댓값 힙
'''

import sys
import heapq

input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(arr, (abs(x), x))
    else:
        if not arr:
            print(0)
        else:
            print(heapq.heappop(arr)[1])
