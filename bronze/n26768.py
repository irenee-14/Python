'''
2024.8.19
26768 - H4x0r
'''

s = input()
for x in s:
    if x == 'a':
        print(4, end='')
    elif x == 'e':
        print(3, end='')
    elif x == 'i':
        print(1, end='')
    elif x == 'o':
        print(0, end='')
    elif x == 's':
        print(5, end='')
    else:
        print(x, end='')