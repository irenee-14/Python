'''
2022.11.4
10845 - 큐
'''
import sys
input = sys.stdin.readline

n = int(input())
tmp = []
stack = []
for i in range(n):
    tmp = list(input().split())
    if tmp[0] == 'push':
        stack.insert(0, tmp[1])
        
    elif tmp[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
            
    elif tmp[0] == 'size':
        print(len(stack))
        
    elif tmp[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
            
    elif tmp[0] == 'front':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack) - 1])
            
    elif tmp[0] == 'back':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[0])
