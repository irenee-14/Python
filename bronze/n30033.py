'''
2025.5.19
30033 - Rust Study
'''

N = int(input())
A = list(input().split())
B = list(input().split())
res = 0

for i in range(0, N):
    if int(A[i]) <= int(B[i]):
        res += 1
print(res)
