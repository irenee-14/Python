'''
2025.8.8
6378 - 디지털 루트
'''

while True :
    N = int(input())
    if N == 0 : break
    ans = N
    while ans >= 10 :
        tmp = 0
        while ans > 0 :
            tmp += ans % 10
            ans //= 10
        ans = tmp
    print(ans)
