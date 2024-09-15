'''
2024.9.15
2018 - 수들의 합 5
'''

n = int(input())

start, end, total, cnt = 1, 1, 1, 1

if n == 1 or n == 2:
    print(1)
else:
    while end < n // 2 + 2:
        if total == n:
            cnt += 1
            end += 1
            total += end
        elif total < n:
            end += 1
            total += end
        else:
            total -= start
            start += 1
    print(cnt)