'''
2022.10.3
11866 - 요세푸스 문제 0
'''

from collections import deque

N, K = map(int, input().split())
nums = deque([])
for i in range(1, N+1):
    nums.append(i)

print('<', end='')
while nums:
    for i in range(K-1):
        nums.append(nums[0])
        nums.popleft()
    print(nums.popleft(), end='')
    if nums:
        print(', ', end='')
print('>')

