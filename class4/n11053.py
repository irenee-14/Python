'''
2024.2.16
11053 - 가장 긴 증가하는 부분 수열(dp)
'''
n = int(input())
nums = list(map(int, input().split()))

dp = [0] * n

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))
