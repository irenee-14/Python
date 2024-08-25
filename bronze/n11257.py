'''
2024.8.26
11257 - IT Passport Examination
'''

n = int(input())

for i in range(n):
    a, b, c, d = map(int, input().split())

    tmp = b + c + d
    if tmp < 55 or b / 35 < 0.3 or  c / 25 < 0.3 or d / 40 < 0.3:
        print(f"{a} {tmp} FAIL")
    elif d / 40 >= 0.3 and c / 25 >= 0/3 and b / 35 > 0.3:
        print(f"{a} {tmp} PASS")

