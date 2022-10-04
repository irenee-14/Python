'''
2022.10.4
1920 - 수찾기
'''

import sys
input = sys.stdin.readline

n = int(input())
A = set(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

for i in B:
  print(1) if i in A else print(0)
