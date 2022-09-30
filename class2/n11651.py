'''
2022.9.30
11651 - 좌표 정렬하기2
'''
import sys
input = sys.stdin.readline

n = int(input())

array = []
for i in range(n):
    [x, y] = map(int, input().split())
    array.append([y, x])
array.sort()
#array.sort(key= lambda x : (x[1], x[0]))

for i in range(n):
    print(array[i][1], array[i][0])
