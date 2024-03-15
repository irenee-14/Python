'''
2024.2.7
1699 - 제곱수의 합(dp)
'''
# 1 : 1^2
# 2 : 1^2 + 1^2
# 3 : 1^2 + 1^2 + 1^2
# 4 : 2^2
# 5 : 2^2 + 1^2
# 6 : 2^2 + 1^2 + 1^2
# 7 : 2^2 + 1^2 + 1^2 + 1^2
# 8 : 2^2 + 1^2 + 1^2 + 1^2 + 1^2
# 9 : 3^2

N = int(input())
dp = [i for i in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, i):
        if j * j > i:
            break
        if dp[i] > dp[i - j * j] + 1:
            dp[i] = dp[i - j * j] + 1

print(dp[N])
