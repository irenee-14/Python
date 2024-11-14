'''
2024.11.13
1090 - 체커
'''

# 모든 위치에서
# 모든 친구들의 거리를 계산해서
# 가장 적은 값을 알려주기

###############################
# 1번 아이디어
# x, y를 구분해서 계산해준 뒤에 합쳐서
# 최솟값을 알려주기

###############################
# 2번째 아이디어
# 우리가 한 곳에서 모일 때, 비용을 최소화 하기 위해서는
# 우리의 집 중 한 곳에서 모이면 된다.

###############################
# 3번째 아이디어
# 최소 거리를 계산하고 싶다.
# 2명이 모여야한다.
# 그 점에서, 가까운 두명의 거리만 더해주면 되지 않을까?

# A, B, C
# 각 집에 모이기 위한 최소 비용 순서대로
# [1, 2, 3] / [3, 4 ,5] / [2, 2, 5]

# 두 사람이 모일 수 있는 최소 거리는
# 작은 수 두개 더해서(3, 7, 4) 중에 -> 3!


# 필요한 스킬
# for 반복문
# 입력과 출력
# 배열 List
# 정렬 sort

######################
# 교차점을 포함한 점들에 대해 계싼 필요!

N = int(input())
arr = []
arr_y = []
arr_x = []
res = [-1] * N

for _ in range(N):
    a, b = map(int, input().split())
    arr.append([a, b])
    arr_y.append(b)
    arr_x.append(a)

for y in arr_y:
    for x in arr_x:
        dist = []

        for dx, dy in arr:
            d = abs(dx - x) + abs(dy - y)
            dist.append(d)
        dist.sort()

        tmp = 0
        for i in range(len(arr)):
            tmp += dist[i]
            if res[i] == -1:
                res[i] = tmp
            else:
                res[i] = min(res[i], tmp)
print(*res)