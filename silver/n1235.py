'''
2024.4.12 
1235 - 학생 번호
'''
N = int(input())
people = [input() for _ in range(N)]

num = len(people[0])

for i in range(1, num + 1):
    res = []
    
    for j in range(N):
        if people[j][-i:] in res:
            break 
        else:
            res.append(people[j][-i:])
        
    if len(res) == N:
        print(i)
        break
