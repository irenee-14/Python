'''
2023.3.28
2605 - 줄 세우기
'''

n = int(input())
num = list(map(int, input().split()))
res = []

for i in range(n):
    res.insert(i - num[i], i + 1)
    
print(*res, sep=" ")
