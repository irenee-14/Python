'''
2024.7.11
5426 - 비밀 편지
'''

n = int(input())

for _ in range(n):
    s = input()
    m = int(len(s) ** (1/2))

    res = ""

    for i in range(m, 0, -1):
        for j in range(i, m * m + 1, m):
            res += s[j - 1]
    print(res)