'''
2025.10.7
16428 - A/B - 3
'''

A, B = map(int, input().split())
if B > 0:
    print(A // B)
    print(A % B)

else:
    print(-(A // -B))
    print(A % -B)