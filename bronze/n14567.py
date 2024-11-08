'''
2024.11.8
14567 - 사탕
'''

n = int(input())
res = 0
for A in range(0, n + 1): # A : 0 ~ 6개
    for B in range(0, n + 1):  # A : 0 ~ 6개
        for C in range(0, n + 1):  # A : 0 ~ 6개
            if A + B + C == n:
                if A >= B + 2:
                    if A != 0 and B != 0 and C != 0:
                        if C % 2 == 0:
                            res += 1
print(res)