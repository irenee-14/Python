'''
2024.2.27
15663 - N과  M (9)
'''

n, m = map(int, input().split())

num = list(map(int, input().split()))
num.sort()

visited = [False] * n
res = []

def nm():
    if len(res) == m:
        print(*res)
        return 
    
    pre = 0
    for i in range(n):
        if not visited[i] and pre != num[i]:
            visited[i] = True
            res.append(num[i])
            pre = num[i]
            nm()
            res.pop()
            visited[i] = False
nm()
