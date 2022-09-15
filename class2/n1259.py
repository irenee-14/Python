'''
2022.9.15
1259 - 팰린드롬수
'''

while True:
    num = input()
    if num == '0':
        break
    if num == num[::-1]:
        print('yes')
    else:
        print('no')

