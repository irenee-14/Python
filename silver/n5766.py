'''
2025.5.30
5766 - 할아버지는 유명해!
'''

import sys
from collections import Counter

while True:
    rank = []
    answer = []
    n, m = map(int, sys.stdin.readline().split())

    if n == 0 and m == 0:
        break

    for _ in range(n):
        rank += list(map(int, sys.stdin.readline().split()))

    sorted_count = sorted(Counter(rank).items(), key=lambda x: x[1], reverse=True)
    answer.append(sorted_count[1][0])

    for i in range(2, len(sorted_count)):
        if sorted_count[i][1] != sorted_count[1][1]:
            break
        else:
            answer.append(sorted_count[i][0])

    print(*sorted(answer))
