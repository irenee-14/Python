'''
2025.7.6
5032 - 탄산 음료
'''

e, f, c = map(int, input().split())
n = (e + f) // c + (e + f) % c
res = (e + f) // c
while n // c:
    res += n // c
    n = n // c + n % c
print(res)