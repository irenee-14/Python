'''
2025.1.31
4613 - Quicksum
'''

while True:
    tmp = input().rstrip()
    if tmp == '#':
        break

    res = 0
    for j in range(len(tmp)):
        if tmp[j] != ' ':
            res += (ord(tmp[j]) - 64) * (j + 1)
    print(res)