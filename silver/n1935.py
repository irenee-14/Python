'''
2024.6.12
1935 - 후위 표기식 2
'''

n = int(input())
line = input()
num = []
stack = []

for i in range(n):
    num.append(int(input()))

for x in line:
    if 'A' <= x <= 'Z':
        stack.append(num[ord(x) - 65])
    else:
        b = stack.pop()
        a = stack.pop()

        if x == '+':
            stack.append(a + b)
        elif x == '-':
            stack.append(a - b)
        elif x == '*':
            stack.append(a * b)
        elif x == '/':
            stack.append(a / b)
print('%.2f' % stack[0])

