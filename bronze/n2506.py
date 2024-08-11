'''
2024.8.11
2506 - 점수계산
'''

n = int(input())
s = list(map(int, input().split()))

res = 0
tmp = 0
for i in range(n):
    if s[i] == 0:
        tmp = 0
    else:
        tmp += 1
        res += tmp
print(res)