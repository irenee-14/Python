'''
2024.7.25
1681 - 줄 세우기
'''

N, L = input().split()
N = int(N)

cnt = 0
i = 0
while cnt != N:
    i += 1
    if L in str(i):
        continue
    cnt += 1
print(i)