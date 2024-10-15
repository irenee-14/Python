'''
2024.10.15
2747 - 피보나치 수
'''

n = int(input())
F = [0] * 46
F[0] = 0
F[1] = 1

for i in range(2, 46):
    F[i] = F[i - 1] + F[i - 2]
print(F[n])
