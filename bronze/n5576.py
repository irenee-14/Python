'''
2025.4.4
5576 - 콘테스트
'''

W = []
K = []

for i in range(20):
    if i < 10:
        W.append(int(input()))
    else:
        K.append(int(input()))
K.sort()
W.sort()
print((W[-1] + W[-2] + W[-3]), (K[-1] + K[-2] + K[-3]))