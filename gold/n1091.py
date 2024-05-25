'''
2024.5.25
1091 - 카드 섞기
'''
N = int(input())
# 어느 플레이어에게 가야하는지 
P = list(map(int, input().split()))
# 카드 섞는 방법 i번째 카드 -> s[i] 번째
S = list(map(int, input().split())) 

card = [0, 1, 2] * (N // 3)
fir = P
cnt = 0

while card != P:
    tmp = [0] * N
    
    for i in range(N):
        tmp[S[i]] = P[i]
    if fir == tmp:
        cnt = -1
        break
    
    P = tmp
    cnt += 1
print(cnt)
