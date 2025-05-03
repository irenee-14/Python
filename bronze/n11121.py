'''
2025.5.4
11121 - Communication Channels
'''


t = int(input())
for i in range(t):
    origin, changed = input().split()
    flag = 0
    for i in range(len(origin)):
        if origin[i] != changed[i]:
            flag = 1

    if flag:
        print('ERROR')
    else:
        print('OK')