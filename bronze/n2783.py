'''
2024.8.20
2783 - 삼각 김밥
'''

x, y = map(int, input().split())
res = []
res.append(x/y)
n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    res.append(a/b)
print("{:.2f}".format(min(res) * 1000))