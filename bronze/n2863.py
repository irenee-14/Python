'''
2024.6.19
2863 - 이게 분수?
'''

A, B = map(int , input().split())
C, D = map(int , input().split())
res = [A/C + B/D, C/D + A/B, D/B + C/A, B/A + D/C]
print(res.index(max(res)))
