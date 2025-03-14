'''
2025.3.14
5063 - TGN
'''

case = int(input())

for _ in range(case):
    r, e, c = map(int, input().split())
    if r > e - c:
        print('do not advertise')
    elif r == e - c:
        print('does not matter')
    else:
        print('advertise')