'''
2024.11.16
5356 - Triangles
'''

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n = int(input())
for i in range(n):
    m, al = input().split()
    index = alpha.index(al)

    for j in range(1, int(m) + 1):
        print(alpha[index] * j)
        index += 1
        if index == 26:
            index = 0
    print()
