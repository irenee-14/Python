'''
2022.10.2
10814 - 나이순 정렬
'''

import sys
input = sys.stdin.readline

n = int(input())
people = []
new = []

for i in range(n):
    people.append(list(input().split()))
new = sorted(people, key=lambda x : int(x[0]))
for i in range(n):
    print(new[i][0], new[i][1])
