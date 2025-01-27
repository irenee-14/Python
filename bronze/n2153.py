'''
2025.1.27
2153 - 소수 단어
'''
import math

word = list(input())
l = 0
for x in word:
    if x.islower():
        l += ord(x) - 96
    else:
        l += ord(x) - 38

flag = False

for i in range(2, int(math.sqrt(l)) + 1):
    if l % i == 0:
        flag = True
        break

if flag:
    print('It is not a prime word.')
else:
    print('It is a prime word.')
