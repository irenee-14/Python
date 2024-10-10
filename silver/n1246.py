'''
2024.10.10
1246 - 온라인 판매
'''

N, M = map(int, input().split())
P = []
for i in range(M):
    P.append(int(input()))
P.sort()
res = 0
price = 0

for i in range(M):
    cnt = min(M - i, N)

    if res < P[i] * cnt:
        res = P[i] * cnt
        price = P[i]
print(price, res)