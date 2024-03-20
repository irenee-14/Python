'''
2024.3.20
1015 - 수열정렬
'''
n = int(input())
A = list(map(int, input().split()))

sortA = sorted(A, reverse=False)
P = []
for i in range(n):
    idx = sortA.index(A[i])
    P.append(idx)
    sortA[idx] = -1
    

print(*P)
