'''
2024.11.21
3020 - 이모스의 장애물 경주(개똥벌레)
2.3 _ 누적 합
'''

import sys
input = sys.stdin.readline

N, H = map(int, input().split())
board = [0 for _ in range(H)]

for i in range(N):
    tmp = int(input())
    if i % 2 == 0:
        board[0] += 1
        board[tmp] -= 1
    else:
        board[H - tmp] += 1

prefix = [0 for _ in range(H + 1)]

for i in range(H):
    prefix[i + 1] = prefix[i] + board[i]
prefix = prefix[1:]
print(min(prefix), prefix.count(min(prefix)))