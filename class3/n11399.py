'''
2022.12.13
11399 - ATM
'''
n = int(input())
money = list(map(int, input().split()))
money.sort()
for i in range(1, n):
    money[i] += money[i-1]
print(sum(money))
