'''
2024.1.3
21736 - 헌내기는 친구가 필요해 (BFS)
'''
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
campus = []
start = []

for i in range(N):
    tmp = list(input().strip())
    for j in range(M):
        if tmp[j] == 'I':
            start = [i, j]
            tmp[j] = 1
    campus.append(tmp)

dx, dy = [-1,1,0,0],[0,0,-1,1]
visited = [[0] * M for _ in range(N)]
res = 0
que = deque([start])

while que:
    x, y = que.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < N and 0 <= ny < M:
            if campus[nx][ny] != 'X' and not visited[nx][ny]:
                que.append((nx, ny))
                visited[nx][ny] = 1
                
                if campus[nx][ny] == 'P':
                    res += 1
if res:
  print(res)
else:
  print('TT')
