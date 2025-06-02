'''
2025.6.2
3035 - 스캐너
'''

R, C, ZR, ZC = map(int, input().split())
res = []

for _ in range(R):
    li = input()
    tmp = ""

    for x in li:
        tmp += x * ZC
    for i in range(ZR):
        res.append(tmp)

for i in res:
    print(i)
