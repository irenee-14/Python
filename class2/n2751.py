'''
2022.9.27
2751 - 수 정렬하기 2
'''

import sys

n = int(input())
num_list = []

for _ in range(n):
    num_list.append(int(sys.stdin.readline()))
num_list.sort()
for i in num_list:
    print(i)
