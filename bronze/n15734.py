'''
2025.2.14
15734 - 명장 남정훈
'''

L, R, A = map(int, input().split())
a, b = min(L, R), max(L, R)
t = min(A, b-a)
a += t
A -= t
res = a * 2

if A:
    res += A // 2 * 2
else:
    res += 0
print(res)