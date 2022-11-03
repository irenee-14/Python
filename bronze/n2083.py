'''
2022.11.3
2083 - 럭비클럽
'''

import sys
input = sys.stdin.readline

while True:
    person = list(input().split())
    if person[0] == '#' and int(person[1]) == 0 and int(person[2]) == 0:
        quit()
    if int(person[1]) > 17 or int(person[2]) >= 80:
        print(person[0], 'Senior')
    else:
        print(person[0], 'Junior')
