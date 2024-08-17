'''
2024.8.17
2875 - 대회 or 인턴
'''

n, m, k = map(int, input().split())
res = 0
while n > 0 and m > 0:
    if n - 2 >= 0 and m - 1 >= 0 and n + m - 3 >= k:
        n -= 2
        m -= 1
        res += 1
    else:
        break
print(res)