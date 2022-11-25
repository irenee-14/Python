'''
2022.11.25
1009 - 분산처리
'''

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    aa = a % 10

    if aa == 0:
        print(10)
    elif aa in [1,5,6]:
        print(aa)
    elif aa in [4,9]:
        if (b%2) == 0:
            print(aa**2%10)
        else:
            print(aa)
    else:
        if b%4 == 0:
            print(aa**4 % 10)
        else:
            print(aa**(b%4)%10)