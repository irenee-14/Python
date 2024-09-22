'''
2024.9.22
1789 - 수들의 합
'''

S = int(input())

res = 0
cnt = 0

while True:
    cnt += 1
    res += cnt
    if res > S:
        break

print(cnt - 1)