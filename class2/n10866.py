'''
2022.11.5
10866 - 덱
'''
from collections import deque

import sys
input = sys.stdin.readline

n = int(input())
tmp = []
command = deque()

for i in range(n):
    tmp = list(input().split())
    if tmp[0] == 'push_front':
        command.appendleft(tmp[1])
    elif tmp[0] == 'push_back':
        command.append(tmp[1])

    elif tmp[0] == 'pop_front':
        if len(command) == 0:
            print(-1)
        else:
            print(command.popleft())
    elif tmp[0] == 'pop_back':
        if len(command) == 0:
            print(-1)
        else:
            print(command.pop())

            
    elif tmp[0] == 'size':
        print(len(command))
        
    elif tmp[0] == 'empty':
        if len(command) == 0:
            print(1)
        else:
            print(0)
            
    elif tmp[0] == 'front':
        if len(command) == 0:
            print(-1)
        else:
            print(command[0])
        
    elif tmp[0] == 'back':
        if len(command) == 0:
            print(-1)
        else:
            print(command[-1])
