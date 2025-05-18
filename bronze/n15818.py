'''
2025.5.18
15818 - 오버플로우와 모듈러
'''

N, M = map(int, input().split())
li = list(map(int, input().split()))
res = 1
for n in li:
    res *= n
print(res%M)