'''
2023.3.12
10825 - 국영수
'''

import sys
input = sys.stdin.readline

n = int(input())
student = []

for _ in range(n):
    student.append(list(input().split()))

student.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in student:
    print(i[0])