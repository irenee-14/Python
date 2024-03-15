'''
2024.2.26
15666 - N과 M (12)
'''
n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
res = []

def nm(start):
    if len(res) == m:
        print(*res)
        return
    pre = 0
    for i in range(start, n):
        if pre != num[i]:
            res.append(num[i])
            pre = num[i]
            nm(i)
            res.pop()

nm(0)
