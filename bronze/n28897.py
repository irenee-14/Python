'''
2023.4.23
2897 - 몬스터 트럭
'''

r, c = map(int, input().split())
park = []

for i in range(r):
    park.append(input())
res = [0] * 5

for i in range(r):
    for j in range(c):
        if i + 1 == r or j + 1 == c:
            break
        temp = 0
        if park[i][j] == '#' or park[i][j + 1] == '#' or park[i + 1][j] == '#' or park[i + 1][j + 1] == '#':
            continue
        if park[i][j] == 'X':
            temp += 1
        if park[i + 1][j] == 'X':
            temp += 1
        if park[i][j + 1] == 'X':
            temp += 1
        if park[i + 1][j + 1] == 'X':
            temp += 1
        res[temp] += 1
print(*res, sep="\n")