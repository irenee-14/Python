'''
2022.11.29
9375 - 패션왕 신해빈
'''
from collections import defaultdict

n = int(input())

for _ in range(n):
    N = int(input())
    dic = defaultdict(int)
    for _ in range(N):
        a, b = input().split()
        dic[b] += 1
    cnt = 1
    
    for k in dic:
        cnt *= (dic[k]+1)
    print(cnt-1)
