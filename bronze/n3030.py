'''
2025.1.22
3040 - 백설공주와 일곱 난쟁이
'''

people = [int(input()) for _ in range(9)]

s = sum(people) - 100

for i in range(9):
    for j in range(i + 1, 9):

        if people[i] + people[j] == s:
            people[i] = 0
            people[j] = 0

            for k in range(9):
                if people[k] != 0:
                    print(people[k])
            exit()

