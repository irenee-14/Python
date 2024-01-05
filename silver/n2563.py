'''
2023.3.20
2563 - 색종이
'''

paper = [[0] * 101 for i in range(101)]

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(10):
        for j in range(10):
            paper[a + i][b + j] = 1
res = 0
for x in paper:
    res += sum(x)
print(res)