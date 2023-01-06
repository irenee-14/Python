'''
2023.1.6
14656 - 조교는 새디스트야!!
'''

import sys
input = sys.stdin.readline

n = int(input())
student = list(map(int, input().split()))
cnt = 0

for i in range(n):
    if student[i] != i + 1:
        cnt += 1
print(cnt)
