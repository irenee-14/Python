''''
2025.1.7
18258 - 큐 2
'''

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
q = deque()

for i in range(n):
    word = input().split()
    if word[0] == "push":
        q.append(word[1])
    elif word[0] == "pop":
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif word[0] == "size":
        print(len(q))
    elif word[0] == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif word[0] == "front":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif word[0] == "back":
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])


