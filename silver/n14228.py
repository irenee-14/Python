'''
2024.4.26
14248 - 점프 점프
'''

n = int(input())
A = list(map(int, input().split()))
s = int(input())

q = [s - 1]

visited = [0] * n
visited[s - 1] = 1

while q:
    tmp = q.pop()
    for x in [tmp - A[tmp], tmp + A[tmp]]:
        if 0 <= x < n and not visited[x]:
            visited[x] = 1
            q += [x]
print(sum(visited))