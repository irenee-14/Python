'''
2025.5.29
14495 - 피보나치 비스무리한 수열
'''

n = int(input())

fi = [1 for i in range(n + 1)]

for i in range(4, n + 1):
    fi[i] = fi[i-1] + fi[i - 3]
print(fi[n])
