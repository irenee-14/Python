'''
2025.7.21
15813 - 너의 이름은 몇 점이니?
'''

count = int(input())

name = list(input())
res = []

for i in name:
    res.append(ord(i)-64)

print(sum(res))
