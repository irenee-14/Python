'''
2024.6.30
30031 - 지폐 세기
'''

n = int(input())
res = 0
for _ in range(n):
    w, h = map(int, input().split())
    if w == 136:
        res += 1000
    elif w == 142:
        res += 5000
    elif w == 148:
        res += 10000
    elif w == 154:
        res += 50000
print(res)

