'''
2022.10.1
10989 - 수 정렬하기 3
'''

import sys
input = sys.stdin.readline
n = int(input())

num = [0] * 10001
for i in range(n):
    input_num = int(input())
    num[input_num] = num[input_num] + 1

for i in range(10001):
    if num[i] != 0:
        for j in range(num[i]):
            print(i)
