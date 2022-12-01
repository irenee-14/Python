'''
2022.12.1
1931 - 회의실 배정
'''
import sys
input = sys.stdin.readline

N = int(input())
time = []
for _ in range(N):
    start, end = map(int, input().split())
    time.append([start, end])
# 시작시간으로 정렬
time = sorted(time, key=lambda x: x[0])
# 끝나는 시간으로 정렬
time = sorted(time, key=lambda x: x[1])

last = 0
cnt = 0

for i, j in time:
    if i >= last:
        cnt += 1
        last = j
print(cnt)