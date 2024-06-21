'''
2024.6.21
2010 - 플러그
'''

import sys

n = int(input())
res = 0

for _ in range(n) :
  res += int(sys.stdin.readline())

print(res - (n - 1))