'''
2025.1.19
10448 - 유레카이론
'''

tri = [n * (n + 1) // 2 for n in range(1, 46)]
eureka = [0] * 1001

for i in tri:
    for j in tri:
        for k in tri:
            if i + j + k <= 1000:
                eureka[i + j + k] = 1

T = int(input())
for _ in range(T):
    print(eureka[int(input())])
