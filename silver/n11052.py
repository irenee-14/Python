'''
2024.3.22
11052 - 카드 구매하기
'''
# dp[i] = dp[i-j] + p[j]

N = int(input())
p = list(map(int, input().split()))
p.insert(0, 0)
dp = p
for i in range(1, N + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + p[j])
        # dp[i-j] + p[j] : dp[i - 1] + p[1], dp[i - 2] + p[2] ....
print(dp[N])