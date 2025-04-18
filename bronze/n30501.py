'''
2025.4.18
30501 - 관공... 어찌하여 목만 오셨소...
'''

import sys

N = int(input())

target = ''

for _ in range(N):
    name = sys.stdin.readline().rstrip()

    if 'S' in name:
        target = name

print(target)