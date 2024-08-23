'''
2024.8.22
16088 - Finding Your Coach
'''

n = int(input())

for i in range(n):
    l, r, n, m = map(int, input().split())

    tmp = abs(n - m)
    if n == m:
        print('G')
    elif tmp < l and tmp > r and n - l > 0:
        print('L')
    elif tmp > l and tmp < r and n + r > 0:
        print('R')
    else:
        print('E')