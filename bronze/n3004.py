'''
2024.10.27
3004 - 체스판 조각
'''

N = int(input())
ans = 1
a = 1
for i in range(N):
    ans += a
    if i % 2 == 0:
        a += 1
print(ans)
