'''
2024.7.8
10395 - Automated Checking Machine
'''

X = list(map(int, input().split()))
Y = list(map(int, input().split()))
for i in range(5):
    X[i] += Y[i]
print('Y' if X.count(1) == 5 else 'N')