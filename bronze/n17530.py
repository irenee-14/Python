'''
2025.11.13
17530 - Buffon
'''

N = int(input())
v = [int(input()) for _ in range(N)]

carlos = v[0]
vote = max(v)

if vote <= carlos:
    print('S')
else:
    print('N')