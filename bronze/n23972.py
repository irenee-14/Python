'''
2024.11.7
23972 - 악마의 제안
'''

k, n = map(int, input().split())

if n == 1:
    print(-1)
else:
    a = (k * n) // (n - 1)
    if (k * n) % (n-1):
        a += 1
    print(a)
