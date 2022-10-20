'''
2022.10.20
18111 - 마인크래프트
'''
import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
block = []
answer = sys.maxsize
floor = 0

for _ in range(N):
    block.append(list(map(int, input().split())))

for target in range(257):
    min_target, max_target = 0, 0
    for i in range(N):
        for j in range(M):
            if block[i][j] >= target:
                max_target += block[i][j] - target
            else:
                min_target += target - block[i][j]

    if max_target + B >= min_target:
        if min_target + (max_target * 2) <= answer:
            answer = min_target + (max_target * 2)
            floor = target
print(answer, floor)

#print(ground)
