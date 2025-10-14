'''
2025.10.14
25630 - 팰린드롬 소떡소떡
'''

N = int(input())
stst = list(input())
cnt = 0

for i in range(N // 2):
    if stst[i] != stst[-1 - i]:
        cnt += 1

print(cnt)