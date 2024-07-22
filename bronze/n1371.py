'''
2024.7.22
1371 - 가장 많은 글자
'''
import sys

s = sys.stdin.read()
li = [0]*26
for c in s:
    if c.islower():
        li[ord(c)-97] += 1
for i in range(26):
    if li[i] == max(li):
        print(chr(97 + i), end='')