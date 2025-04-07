'''
2025.4.7
23808 - 골뱅이 찍기 - ㅂ
'''

N = int(input())

for i in range(2 * N):
    print('@' * N + '   ' * N + '@' * N)

for i in range(N):
    print('@' * (5 * N))

for i in range(N):
    print('@' * N + '   ' * N + '@' * N)

for i in range(N):
    print('@' * (5 * N))