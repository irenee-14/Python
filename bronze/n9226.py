'''
2025.2.18
9226 - 도깨비말
'''

import sys
from collections import deque

vowel = ['a', 'e', 'i', 'o', 'u']
input = sys.stdin.readline

while True:
    line = input().rstrip()
    if line == '#':
        break

    if line[0] in vowel:
        print(line + "ay")
    else:
        for i in range(len(line)):
            if line[i] in vowel:
                print(line[i:] + line[:i] + "ay")
                break
        else:
            print(line + "ay")
