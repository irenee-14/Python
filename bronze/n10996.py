'''
2024.7.16
10996 - 별 찍기 - 21
'''

n = int(input())

for _ in range(n):
    print('* ' * (n - n // 2))
    print(' *' * (n // 2))