'''
2025.6.30
14579 - 덧셈과 곱셈
'''

a, b = map(int, input().split())
res = 1
for i in range(a, b+1):
    res *= sum([j for j in range(1, i+1)])
print(res % 14579)