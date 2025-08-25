'''
2025.8.25
14910 - 오르막
'''

N = list(map(int,input().split()))
A = sorted(N)
if N == A:
    print('Good')
else:
    print('Bad')