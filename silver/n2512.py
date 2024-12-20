'''
2024.12.20
2512 - 예산
'''

N = int(input())
num = sorted(list(map(int, input().split())))
M = int(input())

s = 0
e = max(num)

if sum(num) <= M:
    print(max(num))
else:
    while s <= e:
        mid = (s + e) // 2
        tmp = 0
        for x in num:
            tmp += min(mid, x)

        if tmp > M:
            e = mid - 1
        else:
            s = mid + 1
    print(e)


