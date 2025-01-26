'''
2025.1.26
2979 - 트럭 주차
'''

a, b, c = map(int,input().split())
time = [0]*100
res = 0

for _ in range(3):
    start, end = map(int, input().split())
    for i in range(start, end):
        time[i] += 1

for j in time:
    if j == 0:
        res += 0
    elif j == 1:
        res += a
    elif j == 2:
        res += b * 2
    elif j == 3:
        res += c*3

print(res)