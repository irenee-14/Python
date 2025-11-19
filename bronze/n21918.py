'''
2025.11.19
21918 - 전구
'''

n, m = map(int, input().split())
light = [0] + list(map(int, input().split()))
for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        light[b] = c

    elif a == 2:  # 전구 상태 변경
        for i in range(b, c + 1):
            if light[i] == 0:
                light[i] = 1
            elif light[i] == 1:
                light[i] = 0

    elif a == 3:
        for i in range(b, c + 1):
            if light[i] == 1:
                light[i] = 0
    elif a == 4:
        for i in range(b, c + 1):
            if light[i] == 0:
                light[i] = 1

for i in range(1, n + 1):
    print(light[i], end=' ')
