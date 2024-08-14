'''
2024.8.14
1731 - 추론
'''

n = int(input())
li = []
for _ in range(n):
    li.append(int(input()))

res = li[-1]
if li[2] - li[1] == li[1] - li[0]:
    res += li[1] - li[0]
elif li[2] // li[1] == li[1] // li[0]:
    res *= li[1] // li[0]

print(res)