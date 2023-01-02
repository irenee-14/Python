'''
2023.1.2
18870 - 좌표 압축
'''

import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))

sorted_l = sorted(set(l))
dic = {sorted_l[i] : i for i in range(len(sorted_l))}
for i in l:
    print(dic[i], end= ' ')
