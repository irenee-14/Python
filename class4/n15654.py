'''
2023.12.27
15654 - N과 M (5)
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int , input().split()))
num.sort()

def dfs():
    if len(res) == m:
        print(' '.join(map(str, res)))
        return
    
    for i in range(n):
        if visited[i] == 0:
            res.append(num[i])
            visited[i] = 1
            dfs()
            visited[i] = 0
            res.pop()


visited = [0] * n
res = []
dfs()
