'''
2024.2.2
13023 - ABCDE (dfs)
'''

import sys
input = sys.stdin.readline

## ----------------------------

def dfs(i, dep):
    global res
    
    if dep == 4:
        res = True
        return
    
    for x in friend[i]:
        if not visited[x]:
            visited[x] = True
            dfs(x, dep+1)
            visited[x] = False

## ----------------------------

n, m = map(int, input().split())
friend = [[] for _ in range(n)]

visited = [False for _ in range(n)]
res = 0


for i in range(m):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)
    
for i in range(n):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False
    if res:
        break

if res:
    print(1)
else: 
    print(0)
