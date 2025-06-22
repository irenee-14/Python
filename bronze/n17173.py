'''
2025.6.22
17173 - 배수들의 합
'''

N, M = map(int, input().split())
li = list(map(int, input().split()))
res = 0
for i in range(1, N+1):
    for n in li:
        if i%n == 0:
            res += i
            break
print(res)