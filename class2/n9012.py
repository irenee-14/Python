'''
2022.10.10
9012 - 괄호
'''

T = int(input())
for _ in range(T):
    PS = list(input())
    sum = 0
    for x in PS:
        if x == '(':
            sum += 1
        elif x == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')
