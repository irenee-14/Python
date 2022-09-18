'''
2022.9.17
2609 - 최대공약수와 최소공배수
'''

a, b = map(int, input().split())

n, m = max(a, b), min(a, b)

while m > 0:
    n, m = m, n % m

print(n)
print((a * b) // n)
