'''
2024.5.18
1475 - 방 번호
'''
N = list(input())
num = [0 for _ in range(10)]
for i in range(len(N)):
    if N[i] == '6' or N[i] == '9':
        if num[6] <= num[9]:
            num[6] += 1 
        else:
            num[9] += 1
    else:
        num[int(N[i])] += 1 

print(max(num))
