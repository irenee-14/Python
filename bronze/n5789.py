'''
2025.2.26
5789 - 한다 안한다
'''

t = int(input())

for _ in range(t):
    n = list(input())
    k = len(n) // 2 - 1

    if n[k] == n[-k-1]:
        print('Do-it')
    else:
        print('Do-it-Not')