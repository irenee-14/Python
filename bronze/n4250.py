'''
2025.5.9
4150 - 피보나치 수
'''

n = int(input())

data = [0, 1, 1]
for i in range(3, n + 1):
    data.append(data[i-1] + data[i-2])

print(data[n])