'''
2024.2.24
5635 - 생일
'''
n = int(input())

people = []
for _ in range(n):
    name, day, month, year = input().split()
    people.append([int(year), int(month), int(day), name])
people.sort()
print(people[-1][3])
print(people[0][3])