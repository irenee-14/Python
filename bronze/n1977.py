'''
2025.9.9
1977 - 완전제곱수
'''

M = int(input())
N = int(input())
sqrt = []
for i in range(M, N+1):
    T = int(i ** 0.5) ** 2
    if i == T:
        sqrt.append(i)

if sqrt:
    print(sum(sqrt))
    print(min(sqrt))
else:
    print(-1)
