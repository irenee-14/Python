'''
2022.12.14
9461 - 파도반  수열
'''
import sys
input = sys.stdin.readline

T = int(input())

tmp = [1,1,1,2,2]

# P[N] = P[N-1] + P[N-5]
for i in range(5, 100):
    tmp.append(tmp[i-1]+tmp[i-5])
    
for _ in range(T):
    n = int(input())
    print(tmp[n-1])
