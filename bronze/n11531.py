'''
2025.4.13
11531 - ACM 대회 채점
'''

acm = []
cnt = 0
res = 0

while True:
    try:
        a, b, c = input().split()
        if c == 'right':
            cnt += acm.count(b) * 20 + int(a)
            res += 1
        acm.append(b)
    except:
        break
print(res, cnt)
