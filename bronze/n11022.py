'''
2025.2.29
11022 - A + B - 8
'''

t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print("Case #",i + 1, ": ", a, " + ", b, " = ", a + b, sep='')