'''
2023.1.21
11724 - 연결 요소의 개수
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(start, depth):
    visited[start] = 1
    for i in graph[start]:
        if not visited[i]:
            dfs(i, depth + 1)


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

visited = [0] * (n + 1)
count = 0

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    if not visited[i]:
        dfs(i, 0)
        count += 1
print(count)