'''
2024.9.29
9635 - Balloons Colors
'''

T = int(input())
for _ in range(T):
    N, X, Y = map(int, input().split())
    problem = list(map(int, input().split()))

    if problem[0] == X and problem[-1] == Y:
        print('BOTH')
    elif problem[0] == X:
        print('EASY')
    elif problem[-1] == Y:
        print('HARD')
    else:
        print('OKAY')

