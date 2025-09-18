'''
2025.9.18
1252 - 이진수 덧셈
'''

A, B = map(str, input().split())
A = int(A, 2)
B = int(B, 2)
C = A + B

print(bin(C)[2:])