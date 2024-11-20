'''
2024.11.20
2259 - 수열 (누적합)
'''

N, K = map(int, input().split())
nums = list(map(int, input().split()))

prefix = [0 for _ in range(N + 1)]

for i in range(N):
    prefix[i + 1] = prefix[i] + nums[i]
res = []
for i in range(K, N + 1):
    res.append(prefix[i] - prefix[i - K])
print(max(res))
