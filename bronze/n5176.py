'''
2025.3.15
5176 - 대회 자리
'''

k = int(input())

for _ in range(k):
    p, m = map(int, input().split())
    data = [0] * (m + 1)
    count = 0

    for _ in range(p):
        tmp = int(input())
        if data[tmp] == 0:
            data[tmp] = 1
        else:
            count += 1
    print(count)