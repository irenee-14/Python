'''
2023.4.15
1934 - 최소공배수
'''

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    res = a * b

    while b > 0:
        a, b = b, a % b
    print(res//a)