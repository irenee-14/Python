'''
2025.1.21
11021 - A + B - 7
'''

T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    print("Case #", i + 1 , ": ", a + b, sep='')