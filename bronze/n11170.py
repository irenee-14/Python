'''
2024.3.26
11170 - 0의 개수
'''
n = int(input())

for i in range(n):
    n, m = map(int, input().split())
    cnt = 0
    for j in range(n, m + 1):
        x = str(j)
        cnt += x.count('0')
    print(cnt)
    
