'''
2022.11.13
1247 - 부호
'''

import sys
input = sys.stdin.readline

for _ in range(3):
    N = int(input())
    sum = 0
    for i in range(N):
        sum += int(input())
    if sum == 0:
        print('0')
    elif sum > 0:
        print('+')
    else:
        print('-')