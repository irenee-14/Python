'''
2024.11.21
2304 - 창고 다각형
'''

N = int(input())
block = [list(map(int, input().split())) for _ in range(N)]

max_x = 0
max_y = 0
max_index = 0

block.sort(key= lambda x:x[0])
for i in range(N):
    if block[i][1] > max_y:
        max_y = block[i][1]
        max_x = block[i][0]
        max_index = i

min_x = block[0][0]
min_y = block[0][1]

res = 0
for i in range(max_index + 1):
    if min_y < block[i][1]:
        res += min_y * (block[i][0] - min_x)
        min_y = block[i][1]
        min_x = block[i][0]

min_x = block[-1][0]
min_y = block[-1][1]

for i in range(N - 1, max_index - 1, -1):
    if min_y < block[i][1]:
        res += min_y * (min_x - block[i][0])
        min_y = block[i][1]
        min_x = block[i][0]

print(res + (min_x + 1 - max_x) * max_y)