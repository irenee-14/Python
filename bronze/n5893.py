'''
2022.12.4
5893 - 17배
'''

import sys
input=sys.stdin.readline

N = int(input(), 2)

result = N * 17

print(bin(result)[2:])
