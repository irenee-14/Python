'''
2025.4.22
1337 - 올바른 배열
'''

N = int(input())
nums = []
for i in range(N):
    nums.append(int(input()))
nums.sort()

res = 5
for i in range(N):
    cnt = 0
    for j in range(nums[i], nums[i] + 5):
        if j not in nums:
            cnt += 1
    res = min(res, cnt)

print(res)