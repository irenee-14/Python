'''
2024.5.4 
1159 - 농구경기
'''
n = int(input())
player = []
res = []

for _ in range(n):
    a = input()
    player.append(a[0])

first = set(player)

for i in first:
    if player.count(i) >= 5:
        res.append(i)
res.sort()
if len(res) > 0:
    print(*res, sep="")
else:
    print("PREDAJA")
