'''
2024.11.25
2355 - 시그마
'''

A, B = map(int, input().split())
if A > B:
    A, B = B, A
print((B - A + 1) * (A + B) // 2)