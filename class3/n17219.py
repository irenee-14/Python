'''
2022.12.8
17219 - 비밀번호 찾기
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
site = {}

for _ in range(N):
    key, value = input().split()
    site[key] = value

for _ in range(M):
    find = input().rstrip()
    print(site[find])
