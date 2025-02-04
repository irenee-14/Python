'''
2025.2.4
2774 - 아름다운 수
'''

t = int(input())

for _ in range(t):
    x = input()
    data = []
    res = 0

    for i in range(len(x)):
        tmp = int(x[i])
        if tmp not in data:
            res += 1
            data.append(tmp)

    print(res)
