'''
2025.9.30
15995 - 잉어역수 구하기
'''

a, m = map(int, input().split())
for i in range(1, 10001):
    if a * i % m == 1:
        print(i)
        break