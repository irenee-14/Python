'''
2024.9.30
2399 - 거리의 합
'''

n = int(input())
nums = list(map(int, input().split()))
nums.sort()

res = 0
for i in range(n):
    res += (nums[i] - nums[i - 1]) * i * (n - i)
print(res * 2)