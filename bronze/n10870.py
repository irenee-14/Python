'''
2023.3.17
10870 - 피보나치 수 5
'''

n = int(input())

fibo = [0, 1]

for i in range(2, n + 1):
    fibo.append(fibo[i - 2] + fibo [i - 1])
print(fibo[n])