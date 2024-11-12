'''
2024.11.12
1773 - 폭죽쇼
'''

N, C = map(int, input().split())
fire = [0] * (C + 1)

for _ in range(N):
    time = int(input())
    if time == 1:
        print(C)
        exit()
    else:
        for i in range(time, C + 1, time):
            fire[i] = 1
print(sum(fire))
