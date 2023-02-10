'''
2023.1.28
17626 - Four Squares
'''

#  자신의 수에서 그보다 작은 수의 제곱수를 뺀 것의 최소를 구하고 거기에 한개를 더해주면
#  d[i - (j**2)] + 1


n = int(input())

square = [0] * (n + 1)

square[1] = 1

for i in range(2, n + 1):
    j = 1
    min_n = 4
    while(j**2 <= i):
        tmp = square[i - j**2]
        min_n = min(min_n, tmp)
        j += 1
    square[i] = min_n + 1  

print(square[n])
