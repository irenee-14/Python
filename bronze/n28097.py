'''
2024.7.12
28097 - 모범생 포닉스
'''

n = int(input())
t = list(map(int, input().split()))

res = 0

for i in range(n):
    res += t[i]
    if i != n - 1:
        res += 8
print(res // 24, res %24)