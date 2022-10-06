'''
2022.10.5
2164 - 카드 2
'''
from collections import deque

n = int(input())

que = deque([i for i in range(1,n+1)])

while len(que) > 1:
    que.popleft()
    que.append(que.popleft())
print(que[0])
