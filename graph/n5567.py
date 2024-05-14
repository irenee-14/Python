'''
2024.5.14
5567 - 결혼식(bfs)
'''
from collections import deque

n = int(input())
m = int(input())

friend = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)

que = deque()
que.append((1, 0))

visited = [0 for _ in range(n + 1)]
visited[1] = 1

res = 0

while que:
    x, cnt = que.popleft()
    if cnt >= 2:
        continue
    for i in friend[x]:
        if not visited[i]:
            visited[i] = 1
            que.append((i, cnt + 1))
            res += 1
print(res)

