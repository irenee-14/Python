'''
2024.8.23
9295 - 주사위
'''

T = int(input())
for i in range(T):
    n, m = map(int, input().split())
    print('Case ', i + 1, ': ', n + m, sep='')