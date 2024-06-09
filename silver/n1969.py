'''
2024.6.9
1969 - DNA
'''

N, M = map(int, input().split())
arr = []

for i in range(N):
    arr.append(input())

hamming = 0
res = ''
# A C G T
for i in range(M):
    a, c, g, t = 0, 0, 0, 0

    for j in range(N):
        if arr[j][i] == 'A':
            a += 1
        elif arr[j][i] == 'C':
            c += 1
        elif arr[j][i] == 'G':
            g += 1
        elif arr[j][i] == 'T':
            t += 1

    if max(a, c, g, t) == a:
        res += 'A'
        hamming += c + g + t
    elif max(a, c, g, t) == c:
        res += 'C'
        hamming += a + g + t
    elif max(a, c, g, t) == g:
        res += 'G'
        hamming += a + c + t
    elif max(a, c, g, t) == t:
        res += 'T'
        hamming += a + c + g
print(res)
print(hamming)