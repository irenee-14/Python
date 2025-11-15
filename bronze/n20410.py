'''
2025.11.15
20410 - 추첨상 사수 대작전! (Easy)
'''

m, seed, x1, x2 = map(int, input().split())

for a in range(m):
    for c in range(m):
        if x1 == (a * seed + c) % m and x2 == (a * x1 + c) % m:
            print(a, c)
            exit()