'''
2024.4.27 
23351 - 물 주기
'''
N, K, A, B = map(int, input().split())

plants = [K] * N 

start = 1

while True:
    for i in range(A):
        plants[i] += B 
 
    for j in range(N):
        plants[j] -= 1
        
    plants.sort()
    if plants[0] == 0:
        print(start)
        exit()
    start += 1
