'''
2024.12.2
c
'''

T = int(input())

for _ in range(T):
    N = int(input())
    tmp = str(N ** 2)
    if str(N) == tmp[len(tmp) - len(str(N)):]:
        print('YES')
    else:
        print('NO')
