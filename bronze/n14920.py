'''
2025.4.8
14920 - 3n + 1 수열
'''

n = int(input())
i = 1
while n != 1:
    if n % 2:
        n = 3*n + 1
    else:
        n = n//2
    i += 1
print(i)
