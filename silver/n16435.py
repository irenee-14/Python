'''
2024.4.24 
16435 - 스네이크버드
'''
N, L = map(int, input().split())

h = list(map(int,input().split()))
h.sort()

for i in range(N):
    if L >= h[i]:
        L += 1
        
print(L)
