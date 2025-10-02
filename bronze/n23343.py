'''
2025.10.2
23343 - Javascript
'''

x, y = map(str, input().split())
if x.isdigit() and y.isdigit():
    print(int(x) - int(y))
else:
    print('NaN')