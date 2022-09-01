'''
2439 - 별 찍기-2
2022.8.31
'''

n = int(input())
'''
for i in range(n):
    for j in range(n):
        if (n - j - 1) > i:
            print(" ", end="")
        else:
            print("*", end="")
    print("")
'''

for i in range(1, n+1):
    print(" " * (n - i) + "*" * i)
