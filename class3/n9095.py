'''
2022.12.11
9095 - 1, 2, 3 더하기
'''

# 1 -> (1) : 1개
# 2 -> (1+1), (2) : 2개
# 3 -> (1+1+1), (1+2), (2+1), (3) : 4개
# 4 -> (1+1+1+1), (1+1+2), (1+2+1), (1+3), (2+1+1), (2+2), (3+1) -> 7개
#       1 + 2 + 4
def dp(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return dp(n-1) + dp(n-2) + dp(n-3)

T = int(input())

for _ in range(T):
    n = int(input())
    print(dp(n))