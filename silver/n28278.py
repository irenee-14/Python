'''
2025.2.20
28278 - 스택 2
'''

import sys
input = sys.stdin.readline

n = int(input())
stack = []

for i in range(n):
    m = list(map(int, input().split()))
    if m[0] == 1:
        stack.append(m[1])
    elif m[0] == 2:
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif m[0] == 3:
        print(len(stack))
    elif m[0] == 4:
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    else:
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)

