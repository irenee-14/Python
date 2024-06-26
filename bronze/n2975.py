'''
2024.6.26
2975 - Transactions
'''

while True:
    a, o, b = input().split()
    a, b = int(a), int(b)
    res = 0
    if a == 0 and b == 0:
        break
    if o == 'W':
        res = a - b
    elif o == 'D':
        res = a + b

    if res < -200:
        print('Not allowed')
    else:
        print(res)