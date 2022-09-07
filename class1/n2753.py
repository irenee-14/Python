'''
2022.9.7
2753 - 윤년
'''

year = int(input())
if ((0 == year % 4) and (year % 100 != 0)) or (year % 400 == 0):
    print(1)
else:
    print(0)