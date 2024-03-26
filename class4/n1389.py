'''
2024.3.26
1389 - 케빈 베이컨의 6단계 법칙(bfs)
'''
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def bfs(graph, start):
    num = [0] * (N + 1)
    que = deque()
    visited = [start]
    que.append(start)
    
    while que:
        a = que.popleft()
        for i in graph[a]:
            if i not in visited:
                num[i] = num[a] + 1 
                visited.append(i)
                que.append(i)
    return sum(num)

res = []
for i in range(1, N + 1):
    res.append(bfs(graph, i))
    
print(res.index(min(res))+1)
