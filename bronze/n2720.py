'''
2024.4.21
2720 - 세탁소 사장 동혁
'''
n = int(input())

for _ in range(n):
    money = int(input())
    for i in [25, 10, 5, 1]:
        print(money // i, end=' ')
        money = money % i
