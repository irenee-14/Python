''''
2025.3.19
11557 - Yangjojang of The Year
'''

T = int(input())
for _ in range(T):
    N = int(input())
    max = 0
    res = ""

    for _ in range(N):
        name, num = input().split()
        num = int(num)
        if num > max:
            max = num
            res = name
    print(res)