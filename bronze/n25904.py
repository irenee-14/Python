'''
2024.5.16
25904 - 안녕 클레오파트라 세상에서 제일가는 포테이토칩
'''
N, X = map(int, input().split())
T = list(map(int, input().split()))

res = 0
while True:
    for i in range(N):
        if X <= T[i]: 
            X += 1
        else:
            print(i + 1)
            exit(0)
        
