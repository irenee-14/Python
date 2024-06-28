'''
2024.6.28
8710 - Koszykarz
'''
k, w, m = map(int, input().split())
print((w - k)//m + (1 if (w - k) % m else 0))
