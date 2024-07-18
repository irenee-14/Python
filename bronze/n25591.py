'''
2024.7.1
25591 - 푸앙이와 종윤이
'''

i, j = map(int, input().split())

a = 100 - i
b = 100 - j
c = 100 - (a + b)
d = a * b

q = d // 100
r = d % 100

print(a, b, c, d, q, r)
print(c + q, r)