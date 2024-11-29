'''
2024.11.29
12865 - 평범한 배낭
'''

# 3.2 4번 문제

def recur(idx, weight):

    if weight > B:
        return -9999999
    if idx == N:
        return 0

    if dp[idx][weight] != -1:
        return dp[idx][weight]

    # 물건을 넣은 경우
    # 물건을 안 넣은 경우
    dp[idx][weight] = max(recur(idx + 1, weight + items[idx][0]) + items[idx][1], recur(idx + 1, weight))
    return dp[idx][weight]

N, B = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]

# weight가 있으므로 dp 테이블을 2차원으로 만들기

dp = [[-1 for i in range(100_001)] for _ in range(N)]
res = recur(0, 0)
print(res)

