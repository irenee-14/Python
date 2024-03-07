'''
2024.3.7
1158 - 요세푸스 문제
'''
N, K = map(int, input().split())

arr = [i for i in range(1, N + 1)]
res = []
idx = 0
while len(arr):
    idx += K - 1
    if idx >= len(arr):
        idx = idx % len(arr)
    res.append(str(arr.pop(idx)))
    
print("<",", ".join(res),">", sep='')
