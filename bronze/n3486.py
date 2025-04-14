'''
2025.4.14
3486 - Adding Reversed Numbers
'''


for _ in range(int(input())):
    a, b = input().split()
    a, b = int(a[::-1]), int(b[::-1])
    res = int(str(a + b)[::-1])
    print(res)
