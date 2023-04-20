'''
2023.4.20
5533 - 유니크
'''
n = int(input())
game =[[], [], []]
res = []

for i in range(n):
    a, b, c = map(int, input().split())
    game[0].append(a)
    game[1].append(b)
    game[2].append(c)

check = 0
for i in range(n):
    check = 0
    for j in range(3):
        if game[j].count(game[j][i]) == 1:
            check += game[j][i]
    res.append(check)
print(*res, sep="\n")
        
