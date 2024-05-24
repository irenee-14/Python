'''
2024.5.24 
1500 - 최대 곱
'''
s, k = map(int, input().split())

div = s // k
re = s % k 

res = 1
cnt = 0

for i in range(k):
    if cnt < re:
        res *= (div + 1)
        cnt += 1
    else:
        res *= div
print(res)
