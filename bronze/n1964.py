'''
2024.7.17
1964 - 오각형, 오각형, 오각형…
'''

n = int(input())
# 5, 12, 22
# 5, 5 + 7, 5 + 7 + 10
res = 5
tmp = 7
for i in range(1, n):
    res += tmp
    tmp += 3
print(res % 45678)