'''
2025.8.13
28289 - 과 조사하기
'''

P = int(input())
result = [0] * 4

for _ in range(P):
    student = list(map(int, input().split()))

    if student[0] == 1:
        result[3] += 1
        continue

    if student[1] == 1 or student[1] == 2:
        result[0] += 1
    elif student[1] == 3:
        result[1] += 1
    else:
        result[2] += 1

for r in result:
    print(r)