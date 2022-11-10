'''
2022.11.10
15829 - Hashing
'''

import sys
input = sys.stdin.readline

L = int(input())
st = input()
res = 0
for i in range(L):
    res += (ord(st[i]) - 96) * (31 ** i)
print(res % 1234567891)