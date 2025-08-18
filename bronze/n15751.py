'''
2025.8.18
15751 - Teleportation
'''

a, b, x, y = map(int, input().split())
a, b = min(a, b), max(a, b)
x, y = min(x, y), max(x, y)

dis = b - a
tele = abs(x - a) + abs(y - b)
res = min(dis, tele)

print(res)