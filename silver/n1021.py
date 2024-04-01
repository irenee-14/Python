'''
2024.4.1
1021 - 회전하는 큐
'''

from collections import deque

N, M = map(int, input().split())
pos = list(map(int, input().split()))

dq = deque([i for i in range(1, N + 1)])

cnt = 0
for idx in pos:
    while True:
        if dq[0] == idx:
            dq.popleft()
            break
        else:
            if dq.index(idx) <= len(dq)//2:
                dq.rotate(-1)
            else:
                dq.rotate(1)
            cnt += 1
print(cnt)