'''
2024.11.4
1011 - Fly me to the Alpha Centauri
'''

n = int(input())
for i in range(n):
    x, y = map(int, input().split())

    dis = y - x
    step = 1
    cnt = 0
    tmp = 0

    while tmp < dis:
        cnt += 1
        tmp += step

        if cnt % 2 == 0:
            step += 1
    print(cnt)