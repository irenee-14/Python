'''
2022.9.29
11650 - 좌표 정렬하기
'''
import sys
input = sys.stdin.readline

n = int(input())

array = []
for i in range(n):
    [x, y] = map(int, input().split())
    array.append([x, y])
sort_array = sorted(array)

for i in range(n):
    print(sort_array[i][0], sort_array[i][1])
