'''
2022.10.9
2805 - 나무 자르기
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
height = list(map(int, input().split()))

start, end = 0, max(height)

while start <= end:
    mid = (start + end) // 2
    cut = 0
    for i in height:
        if i > mid:
            cut += i - mid
    if cut >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)
