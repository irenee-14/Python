'''
2024.1.4 
15657 - N과 M (8)
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

def dfs(start):
    if len(res) == m:
        print(*res)
        return
    for i in range(start, n):
            res.append(num[i])
            dfs(i)
            res.pop()

res = []
dfs(0)
