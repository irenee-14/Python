'''
2025.5.7
9455 - 박스
'''

T = int(input())
for _ in range(T):
    m, n = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(m)]

    cnt = 0
    for i in range(n):
        bottom = m - 1

        for j in reversed(range(m)):
            if graph[j][i] == 1:
                cnt += bottom - j
                bottom -= 1
    print(cnt)



