'''
2023.3.24
10974 - 모든 순열
'''

def dfs():
   if len(res) == n:
      print(*res)
      return

   for i in range(1, n + 1):
       if vis[i] == 0:
           res.append(i)
           vis[i] = 1
           dfs()
           res.pop()
           vis[i] = 0

n = int(input())
vis = [0 for _ in range(n + 1)]
res = []

dfs()