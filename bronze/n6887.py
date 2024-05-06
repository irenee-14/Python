'''
2024.5.6
6887 - Squares
'''
n = int(input())
i = 1
while i * i <= n:
    i += 1
print("The largest square has side length " + str(i - 1) + ".")

