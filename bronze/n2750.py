'''
2023.2.4
2750 - 수 정렬하기
'''

n = int(input())
num = []

for _ in range(n):
    num.append(int(input()))
num.sort()

print(*num, sep="\n")