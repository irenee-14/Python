'''
2024.6.16
2721 - 삼각수의 합
'''

for _ in range(int(input())):
    n = int(input())
    res = sum(k * sum(range(k + 2)) for k in range(1, n + 1))
    print(res)