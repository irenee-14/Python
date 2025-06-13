'''
2025.6.13
2858 - 기숙사 바닥
'''

R, B = map(int, input().split())
# 2(L + W) - 4 == (L - 2) * (W - 2)
LW = R + B

r = (R + 4) // 2

for i in range(1, r):
    if (r - i) * i == LW:
        print(max(i, r - i), min(i, r - i))
        break