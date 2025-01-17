'''
2025.1.17
1417 - 국회의원 선거
'''

n = int(input())
m = int(input())

vote = []
cnt = 0

for _ in range(n - 1):
    vote.append(int(input()))

vote.sort(reverse=True)

if n == 1:
    print(0)
else:
    while vote[0] >= m:
        m += 1
        vote[0] -= 1
        cnt += 1
        vote.sort(reverse=True)
    print(cnt)