'''
2022.12.19
5586 - JOI와 IOI
'''
alpa = list(input())
J = 0
I = 0

for i in range(0, len(alpa)-2):
    if alpa[i] == 'J' and alpa[i+1] == 'O' and alpa[i+2] == 'I':
        J += 1
        i -= 1
    if alpa[i] == 'I' and alpa[i+1] == 'O' and alpa[i+2] == 'I':
        I += 1
        i -= 1
print(J)
print(I)
