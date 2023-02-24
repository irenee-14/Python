'''
2023.2.24
2444 - 별찍기  - 7
'''
n = int(input())

for i in range(n - 1, -1, -1):
    print(" " * i + "*" * ((n - i) * 2 - 1))
for i in range(1, n):
    print(" " * i + "*" * ((n - i) * 2 - 1))
