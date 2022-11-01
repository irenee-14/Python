'''
2022.10.14
2798 - 블랙잭
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
card = list(map(int, input().split()))
res = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if card[i] + card[j] + card[k] > M:
                continue
            else:
                res = max(res, card[i] + card[j] + card[k])
print(res)
