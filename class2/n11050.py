'''
2022.11.7
11050 - 이항계수1
'''

from math import factorial
n, k = map(int, input().split())
b = factorial(n) // (factorial(k) * factorial(n - k))
print(b)
