'''
2024.9.26
10430 - 나머지
'''

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

print((a + b) % c)
print(((a % c) + (b % c)) % c)
print((a * b) % c)
print(((a % c) * (b % c)) % c)