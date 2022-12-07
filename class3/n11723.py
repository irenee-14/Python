'''
2022.12.7
11723 - 집합
'''
import sys
input = sys.stdin.readline

M = int(input())
s = set()

for i in range(M):
    tmp = input().split()
    
    if len(tmp) == 1:
        if tmp[0] == 'all':
            s = set([i for i in range(1, 21)])
        elif tmp[0]:
            s = set()
    else:
        x = int(tmp[1])
        if tmp[0] == 'add':
            s.add(x) 
        elif tmp[0] == 'remove':
            if x in s:
                s.discard(x)
        elif tmp[0] == 'check':
            print(1 if x in s else 0)
        elif tmp[0] == 'toggle':
            if x in s:
                s.discard(x)
            else:
                s.add(x)
