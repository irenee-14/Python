'''
2024.8.3
9772 - Quadrants
'''

while True:
    x, y = map(float, input().split())

    if x > 0:
        if y > 0:
            print('Q1')
        elif y < 0:
            print('Q4')
    elif x < 0:
        if y > 0:
            print('Q2')
        elif y < 0:
            print('Q3')
    if x == 0 or y == 0:
        print('AXIS')
    if x == 0 and y == 0:
        break