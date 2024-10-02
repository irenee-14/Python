'''
2024.10.2
1049 - 기타줄
'''

n, m = map(int, input().split())

pack = []
one = []

for i in range(m):
    a, b = map(int, input().split())
    pack.append(a)
    one.append(b)

res = 0
pack = min(pack)
one = min(one)

if pack < one * 6:
    if pack < (n % 6) * one:
        res = (n // 6 + 1) * pack
    else:
        res = (n // 6) * pack + (n % 6) *  one
else:
    res = n * one
print(res)


