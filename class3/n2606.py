'''
2023.1.16
2606 - 바이러스
'''

from collections import deque

n = int(input())
m = int(input())

com = [[] for i in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    com[a] += [b]
    com[b] += [a]

visited[1] = 1
q = deque([1])

while q:
    cur = q.popleft()
    for x in com[cur]:
        if visited[x] == 0:
            q.append(x)
            visited[x] = 1
print(sum(visited) - 1)