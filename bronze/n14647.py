'''
2025.2.8
14647 - 준오는 조류혐오야!!
'''

n, m = map(int, input().split())
board = []
r, c = [], []
for i in range(n):
    tmp = list(map(str, input().split()))
    board.append(tmp)

    cnt = 0
    for t in tmp:
        cnt += t.count('9')
    r.append(cnt)

for i in range(m):
    cnt = 0
    for j in range(n):
        cnt += board[j][i].count('9')
    c.append(cnt)

print(sum(r) - max(max(r), max(c)))
