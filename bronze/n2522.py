'''
2023.3.2
2522 - 별찍기 - 12
'''
n = int(input())

for i in range(1, n):
    print(" " * (n - i) + "*" * i)
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * i)
