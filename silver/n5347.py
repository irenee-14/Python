'''
2024.9.25
5347 - LCM
'''
import math

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print(a * b // math.gcd(a, b))