'''
2025.2.25
6996 - 애너그램
'''

import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    a, b = map(str, input().split())

    x = sorted(list(a))
    y = sorted(list(b))

    if x == y:
        print("%s & %s are anagrams." % (a, b))
    else:
        print("%s & %s are NOT anagrams." % (a, b))