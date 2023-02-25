'''
2023.2.25
2445 - 별 찍기 - 8
'''
n = int(input())
for i in range(1, n):
    print('*'*i + ' '*2*(n-i) + '*'*i)
for i in range(n, 0, -1):
    print('*'*i + ' '*2*(n-i) + '*'*i)
