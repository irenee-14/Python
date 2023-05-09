'''
2023.5.9
6359 - 만취한 상범
'''

# 열린 문 0 닫힌 문 1
t = int(input())

for _ in range(t):
    n = int(input())
    door = [0] * (n + 1)
    for i in range(2, n + 1):
        for j in range(i, n + 1):
            if j % i == 0:
                if door[j] == 0:
                    door[j] = 1
                else:
                    door[j] = 0 
    print(door.count(0) - 1)
