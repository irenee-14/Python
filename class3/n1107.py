'''
2023.1.3
1107 - 리모컨
'''

import sys
input = sys.stdin.readline

chanel = int(input())
n = int(input())
if n:
    broken = set(input().split())
else:
    broken = set()

res_min = abs(100 - chanel)

for num in range(1000001):
    for i in str(num):
        if i in broken:
            break
    else:
        res_min = min(res_min, len(str(num)) + abs(num - chanel))

print(res_min)
