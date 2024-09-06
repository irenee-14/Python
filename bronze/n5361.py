'''
2024.9.6
5361 - 전투 드로이드 갸격
'''
price = [350.34, 230.90, 190.55, 125.30, 180.90]

n = int(input())
for i in range(n):
    a = list(map(int, input().split()))
    res = 0
    for i in range(5):
        res += price[i] * a[i]
    print('${:.2f}'.format(res))