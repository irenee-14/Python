'''
2023.4.25
1100 - 하얀 칸
'''

c = []
for _ in range(8):
    c.append(list(map(str, input())))
res = 0
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0 and c[i][j] == 'F':
            res += 1
print(res)