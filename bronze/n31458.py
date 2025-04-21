'''
2025.4.21
31458 - !!초콜릿 중독 주의!!
'''

T = int(input())

for _ in range(T):
    S = input().rstrip()

    sign = 0
    lCnt = 0
    res = 0

    for num in S:
        if sign == 0 and num == "!":
            lCnt += 1
        elif num != "!":
            sign = 1
            res = int(num)
        elif sign == 1 and num == "!":
            res = 1

    if res == 0:
        if lCnt % 2 == 0:
            res = 0
        else:
            res = 1
    else:
        if lCnt % 2 == 0:
            res = 1
        else:
            res = 0
    print(res)