'''
2024.9.19
4447 - 좋은놈 나쁜놈
'''

n = int(input())
for i in range(n):
    name = input()
    lower = name.lower()
    type = ''
    if lower.count('g') > lower.count('b'):
        type = 'GOOD'
    elif lower.count('g') < lower.count('b'):
        type = 'A BADDY'
    else:
        type = "NEUTRAL"
    print('{} is {}'.format(name, type))