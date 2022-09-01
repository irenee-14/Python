'''
2438 - 별 찍기 -1
2022.8.31
'''

'''
n = int(input())
i = 1
while i <= n:
    j = 0
    while j < i:
        print('*', end="")
        j += 1
    print("")
    i += 1
'''

n = int(input())
for i in range(n):
    for j in range(i + 1):
        print('*', end="")
    print("")