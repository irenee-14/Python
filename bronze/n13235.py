'''
2025.3.21
13235 - 팰린드롬
'''

n = input()
value = n[::-1]

if value in n:
    print('true')
else:
    print('false')