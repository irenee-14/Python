'''
2023.4.6
11931 - 수 정렬하기 4
'''
import sys
input = sys.stdin.readline

n = int(input())
num = []

for _ in range(n):
    num.append(int(input()))
num = sorted(num, reverse=True)
print(*num, sep="\n")
