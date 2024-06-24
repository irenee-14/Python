'''
2024.6.24
25625 - 샤틀버스
'''

x, y = map(int, input().split())
if x >= y:
    print(x + y)
elif x < y:
    print(y - x)