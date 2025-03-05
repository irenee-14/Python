'''
2025.3.5
5613 - 계산기 프로그램
'''

res = int(input())
while 1:
    op = input()
    if op == '=':
        break
    n = int(input())
    if op == '+':
        res += n;
    elif op == '-':
        res -= n;
    elif op == '*':
        res *= n;
    elif op == '/':
        res //= n;
print(res)
