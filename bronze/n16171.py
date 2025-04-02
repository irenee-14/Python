'''
2025.4.2
16171 - 나는 친구가 적다 (Small)
'''

S = list(input())
K = input()
new = ''

for s in S:
    if 48 <= ord(s) <= 57:
        continue
    else:
        new += s

if K in new:
    print(1)
else:
    print(0)