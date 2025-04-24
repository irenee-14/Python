'''
2025.4.24
11508 - 2+1 세일
'''

N = int(input())
tmp = []
res = 0

for i in range(N):
    tmp.append(int(input()))
tmp.sort(reverse=True)

for i in range(2, len(tmp), 3):
    res += tmp[i]
print(sum(tmp) - res)