'''
2025.4.1
25400 - 제자리
'''
from collections import deque


n = int(input())
A = deque(list(map(int, input().split())))
cur = 1
cnt = 0

while A:
    x = A.popleft()
    if x == cur:
        cur += 1
    else:
        cnt += 1
print(cnt)


