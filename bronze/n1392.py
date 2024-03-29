'''
2024.3.29
1392 - 노래 악보
'''
N, Q = map(int, input().split())
arr = [int(input()) for _ in range(N)]
for _ in range(Q):
    t = int(input())
    for i in range(N):
        if t < sum(arr[:i+1]):
            print(i+1)
            break