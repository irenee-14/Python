'''
2023.3.18
7785 - 회사에 있는 사람
'''

import sys
input = sys.stdin.readline

people = {}

n = int(input())

for _ in range(n):
    name, log = input().rstrip().split()
    
    if log == 'enter':
        people[name] = 'enter'
    else:
        if people[name]:
            del people[name]
            
people = sorted(people, reverse=True)
print(*people, sep="\n")
