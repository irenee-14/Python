'''
2023.3.25
14501 - 퇴사
'''

n = int(input())
t = []
p = []

for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

dp = [0] * (n + 1)

for i in range(n):
    for j in range(i + t[i], n + 1):
        if dp[j] < dp[i] + p[i]:
            dp[j] = dp[i] + p[i]
print(dp[-1])