'''
2024.2.20
21737 - SMUPC 계산기
'''
import sys
input = sys.stdin.readline

n = input()
line = input()

a = 0
b = 0

oper = ''
c = 0

for x in line:
    if x.isdigit():
        if oper:
            b = b * 10 + int(x)
        else: 
            a = a * 10 + int(x)
    else:
        if oper and oper != 'C':
            if oper == 'S':
                a = a - b
            elif oper == 'M':
                a = a * b
            elif oper == 'U':
                if a < 0 and b != 0:
                    a = ((a * -1) // b) * -1
                elif b != 0:
                    a = a // b
            elif oper == 'P':
                a = a + b
        if x == 'C':
            c = 1
            print(a, end=' ')
        oper = x
        b = 0

if not c:
    print('NO OUTPUT')
