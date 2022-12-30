'''
2022.12.30
2476 - 주사위 게임
'''

dice = int(input())
res = 0

for _ in range(dice):
    a, b, c = map(int, input().split())
    if a == b == c:
        res = max(res, 10000 + a * 1000)
    elif a == b:
        res = max(res, 1000 + a * 100)
    elif a == c:
        res = max(res, 1000 + a * 100)
    elif b == c:
        res = max(res, 1000 + b * 100)
    else:
        res = max(res, 100 * max(a, b, c))
print(res)