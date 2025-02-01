'''
2025.2.1
23813 - 회전
'''

N = input()
x = 0
result = 0
for i in range(len(N)):
    x += int(N[i])
for i in range(len(N)): #15 + 150 + 1500 + 15000 + 150000
    result += (x * (10 ** i))
print(result)