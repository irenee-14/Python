'''
2024.3.21
1735 - 분수 합
'''
def gcd(a, b):
    if a % b == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, a % b)


a, b = map(int, input().split())
c, d = map(int, input().split())

A = a * d + b * c 
B = b * d

N = gcd(A, B) 

print(A // N, B // N)
