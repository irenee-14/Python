'''
2025.11.2
30454 - 얼룩말을 찾아라!
'''

N, L = map(int, input().split())
result = []

for _ in range(N):
    zebra = input() + "0"
    tmp1 = []
    tmp2 = ""
    for i in range(L + 1):
        if zebra[i] == "1":
            tmp2 += "1"
        elif len(tmp2) > 0:
            tmp1.append(tmp2)
            tmp2 = ""

    result.append(len(tmp1))

print(max(result), result.count(max(result)))
