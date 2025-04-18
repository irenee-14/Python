'''
2025.4.27
28352 - 10!
'''

import sys
input = sys.stdin.readline

N = int(input())

res = 1
for i in range(11, N+1):
    res *= i
print(6*res)

