'''
2023.2.26
15964 - 이상한 기호
'''

def oper(a, b):
    print((a + b) * (a - b))

a, b = map(int, input().split())
oper(a, b)