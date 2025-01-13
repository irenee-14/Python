'''
2025.1.13
28279 - 덱2
'''

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
d = deque()

for i in range(N):
    m = list(map(int, input().split()))
    if m[0] == 1:
        d.appendleft(m[1])
    elif m[0] == 2:
        d.append(m[1])
    elif m[0] == 3:
        if d:
            print(d.popleft())
        else:
            print(-1)
    elif m[0] == 4:
        if d:
            print(d.pop())
        else:
            print(-1)
    elif m[0] == 5:
        print(len(d))
    elif m[0] == 6:
        if d:
            print(0)
        else:
            print(1)
    elif m[0] == 7:
        if d:
            print(d[0])
        else:
            print(-1)
    elif m[0] == 8:
        if d:
            print(d[-1])
        else:
            print(-1)