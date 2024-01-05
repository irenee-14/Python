'''
2023.3.19
15649 - N 과 M (1)
'''

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(1, n + 1):
        if visited[i]:
            continue
        visited[i] = 1
        s.append(i)
        dfs()
        s.pop()
        # print(s)
        # print(visited)
        visited[i] = 0

n, m = map(int, input().split())
s = []
visited = [0] * (n + 1)

dfs()