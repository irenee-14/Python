'''
2025.6.4
11816 - 8진수, 10진수, 16진수
'''

X = input()

if X[0] == '0':
    if X[1] == 'x':
        print(int(X, 16))
    else:
        print(int(X, 8))
else:
    print(X)