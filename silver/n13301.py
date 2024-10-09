'''
2024.10.9
13301 - 타일 장식물
'''

n = int(input())

d = [0] * (n + 2)
d[1] = 1

for i in range(2, n + 2):
    d[i] = d[i - 1] + d[i - 2]
print((d[n] + d[n + 1]) * 2)
