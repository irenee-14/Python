'''
2024.7.23
1418 - K - 세준수
'''

n = int(input())
k = int(input())

tmp = [0 for i in range(n + 1)]

for i in range(2, n + 1):
    if tmp[i] == 0:
        for j in range(i, n + 1, i):
            if j % i == 0:
                tmp[j] = max(tmp[j], i)
res = 0
for i in tmp:
    if i <= k:
        res += 1
print(res - 1)
