'''
2024.3.4 
1010 - 다리 놓기
'''
T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    
    res = [[1] * (M + 1) for _ in range(N + 1)]
    
    for i in range(1, M + 1):
        res[1][i] = i
    
    for i in range(2, N + 1):
        for j in range(i + 1, M + 1):
            res[i][j] = res[i][j - 1] + res[i - 1][j - 1]
    print(res[N][M])
