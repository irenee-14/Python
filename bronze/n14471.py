'''
2025.10.28
14471 - 포인트 카드
'''

N, M = map(int, input().split())
card = []
cnt = 0

for _ in range(M):
    A, B = map(int, input().split())
    if A < B:
        card.append([A, B])
    else:
        cnt += 1

card.sort(reverse=True)
res = 0
if M - 1 == cnt:
    print(0)
else:
    for i in range(M - 1 - cnt):
        res += (N - card[i][0])
    print(res)
