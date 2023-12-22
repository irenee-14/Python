'''
2023.12.22 
1149 - RGB 거리
'''

# 3
# 26 40 83
# 49 60 57    49+40   60+26   57+26 
#             89      86      83
# 13 89 99    13+83   89+83   99+83
#             96      172     182
# => 96

# 3
# 1 100 100   
# 100 1 100   101 2   101
# 100 100 1   102 102 3
# => 3

import sys
input = sys.stdin.readline

n = int(input())
rgb = []

for _ in range(n):
    rgb.append(list(map(int, input().split())))

for i in range(1, n):
    rgb[i][0] = min(rgb[i - 1][1], rgb[i - 1][2]) + rgb[i][0]
    rgb[i][1] = min(rgb[i - 1][2], rgb[i - 1][0]) + rgb[i][1]
    rgb[i][2] = min(rgb[i - 1][0], rgb[i - 1][1]) + rgb[i][2]
print(min(rgb[n - 1]))
