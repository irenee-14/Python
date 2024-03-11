'''
2024.3.11
1380 - 귀걸이
'''
cnt = 1
while True:
    n = int(input())
    
    if n == 0:
        break
    
    names = []
    for _ in range(n):
        names.append(input())
    
    earing = []
    for i in range(2 * n - 1):
        earing.append(int(input().split()[0]))
    for i in range(1, n + 1):
        if earing.count(i) % 2 == 1:
            print(cnt, names[i - 1])
    cnt += 1
