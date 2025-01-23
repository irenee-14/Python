'''
2025.1.23
10820 - 문자열 분석
'''

import sys
input = sys.stdin.readline

while True:
    s = input().rstrip('\n')

    if not s:
        break

    cnt = [0] * 4
    for x in s:
        if x.islower():
            cnt[0] += 1
        elif x.isupper():
            cnt[1] += 1
        elif x.isdigit():
            cnt[2] += 1
        else:
            cnt[3] += 1

    print(*cnt, sep=' ')

