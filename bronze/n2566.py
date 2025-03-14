'''
2024.10.7
2566 - 최댓값
'''

table = [list(map(int, input().split())) for _ in range(9)]

max_num = 0
max_row, max_col = 0, 0

for i in range(9):
    for j in range(9):
        if table[i][j] >= max_num:
            max_row = i + 1
            max_col = j + 1
            max_num = table[i][j]
print(max_num)
print(max_row, max_col)