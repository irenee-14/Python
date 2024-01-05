'''
2023.2.19
5585 - 거스름돈
'''

n = 1000 - int(input())
money = [500, 100, 50, 10, 5, 1]
cnt = 0
for x in money:
    if n / x > 0:
        cnt += int(n / x)
        n -= int(n / x) * x
print(cnt)
