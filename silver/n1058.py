'''
2024.4.2
1058 - 친구
'''
N = int(input())
people = [list(input()) for _ in range(N)]
f = [[0] * N for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if people[i][j] == 'Y' or (people[i][k] == 'Y' and people[k][j] == 'Y'):
                f[i][j] = 1

res = 0
for row in f:
    res = max(res, sum(row))
print(res)
    
