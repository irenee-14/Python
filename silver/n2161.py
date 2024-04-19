'''
2024.4.19
2161 - 카드 1
'''

from collections import deque
N = int(input())

q = deque()
for i in range(N):
    q.append(i + 1)

while q:
    print(q.popleft(), end=' ')
    if q:
        tmp = q.popleft()
        q.append(tmp)
    if len(q) == 1:
        print(*q)
        break

