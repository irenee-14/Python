'''
2024.5.23 
1835 - 카드
'''
from collections import deque

N = int(input())
que = deque()
que.append(N)

for i in range(N - 1, 0, -1):
   que.appendleft(i)
   
   for j in range(i):
       que.appendleft(que.pop())
       
print(*que)
