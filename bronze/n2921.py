'''
2024.3.15
2921 - 도미노
'''

n = int(input())
res = 0
for i in range(1, n + 1):
    res += 1.5 * i * (i + 1)
print(int(res))