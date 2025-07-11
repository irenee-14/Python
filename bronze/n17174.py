'''
2025.7.11
17174 - 전체 계산 횟수
'''

N, M = map(int, input().split())
t = N
while N:
    N = N//M
    t += N
print(t)