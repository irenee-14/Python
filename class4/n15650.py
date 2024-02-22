'''
2024.2.22 
15650 - N과 M (2) - (dfs)
'''

n, m = list(map(int,input().split()))
res = []


def dfs(start):
    visited = [False] * (n + 1)
    if len(res) == m:
        print(*res, sep=' ')
        return
    for i in range(start, n + 1):
        if not visited[i]:
            res.append(i)
            visited[i] = True
            dfs(i + 1)
            res.pop()

dfs(1)
