'''
2025.2.10
16462 - '나교수' 교수님의 악필
'''
import math

n = int(input())
res = 0

for i in range(n):
    q = input()

    formatted = ''

    for x in q:
        if x in ['0', '6', '9']:
            formatted += '9'
        else:
            formatted += x

    if 100 < int(formatted):
        formatted = 100
    else:
        formatted = int(formatted)
    res += formatted

avg = res / n
if avg - int(avg) < 0.5:
    print(math.floor(avg))
else:
    print(math.ceil(avg))

