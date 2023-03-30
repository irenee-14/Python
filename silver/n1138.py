'''
2023.3.30
1138 - 한 줄로 서기
'''
n = int(input())
people = list(map(int, input().split()))

line = [0] * n 

for i in range(n):
    cnt = 0
    for j in range(n):
        if cnt == people[i] and line[j] == 0:
            line[j] = i + 1 
            break
        elif line[j] == 0:
            cnt += 1 
print(*line, sep=" ")
