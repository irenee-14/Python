'''
2022.12.5
11047 - 동전 0
'''

N, K = map(int, input().split())
A = []
res = 0

for i in range(N):
    A.append(int(input()))
A = sorted(A, reverse=True)

for i in A:
    res += (K//i)
    K %= i
print(res)