'''
2024.8.15
5724 - 파인만
'''

while True:
    n = int(input())
    if n == 0:
        break
    res = 0
    for i in range(1, n + 1):
        res += (n - i + 1) ** 2
    print(res)