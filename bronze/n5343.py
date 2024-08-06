'''
2024.8.6
5343 - Parity Bit
'''

n = int(input())
for i in range(n):
    s = list(input())
    cnt = 0
    while s:
        tmp = s[:8]
        s = s[8:]
        if tmp.count('1') % 2:
            cnt += 1

    print(cnt)
