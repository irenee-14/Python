'''
2022.1.7
1312 - 소수
'''

a, b, n = map(int, input().split())

for i in range(n):
    a = (a % b) * 10
    res = a // b
print(res)