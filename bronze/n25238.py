'''
2024.12.21
25238 - 가희와 방어율 무시
'''

a, b = map(int, input().split(" "))

if a - (a / 100 * b) >= 100:
    print(0)
elif a - (a / 100 * b) < 100:
    print(1)