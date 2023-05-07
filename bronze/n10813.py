'''
2023.5.7
10813 - 공 바꾸기
'''

n, m = map(int, input().split())
box = [i for i in range(1, n + 1)]
tmp = 0

for i in range(m):
    i, j = map(int, input().split())
    tmp = box[i - 1]
    box[i - 1] = box[j - 1]
    box[j - 1] = tmp

print(*box, sep=' ')
