'''
2025.5.6
16968 - 차량 번호판 1
'''

s = input()

if s[0] == 'c':
    res = 26
else:
    res = 10

for i in range(1, len(s)):
    if s[i] == 'c':
        if s[i - 1] == 'c':
            res *= 25
        else:
            res *= 26
    else:
        if s[i - 1] == 'd':
            res *= 9
        else:
            res *= 10

print(res)