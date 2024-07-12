'''
2024.5.15 
13172 - Σ (페르마의 소정리, 분할정복)
'''
# a / b === a * b^(-1) mod X

# b^(x-2) === b^(-1) mod X
# a / b === a * b^(x-2) mod X

# => a * b^(x-2) % 1_000_000_007 (x = 10^9 + 7)


def cal(N, t):
    if t == 1:
        return N % MOD
    elif t % 2:
        return N * cal(N, t - 1) % MOD
    else:
        p = cal(N, t // 2)
        return p * p % MOD
    

M = int(input())
MOD = 1_000_000_007
res = 0
for i in range(M):
    N, S = map(int, input().split())
    res += S * cal(N, MOD - 2) % MOD
    
print(res % MOD)
