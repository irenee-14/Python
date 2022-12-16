'''
2022.12.2
2579 - 계단 오르기
'''
import sys
input = sys.stdin.readline

step = []
res = []
n = int(input())

for _ in range(n):
    step.append(int(input()))
if len(step) <= 2:
    print(sum(step))
else:
    res.append(step[0])
    res.append(max(step[0]+step[1], step[1]))
    res.append(max(step[0]+step[2], step[1]+step[2]))

    for i in range(3,n):
        res.append(max(res[i-2]+step[i], res[i-3]+step[i]+step[i-1]))
    print(res.pop())
