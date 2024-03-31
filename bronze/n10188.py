'''
2024.3.31
10188 - Quadrilateral
'''

n = int(input())

for i in range(n):
    a, b = map(int,input().split())
    for j in range(b):
        for k in range(a):
            print('X', end='')
        print()
    print()