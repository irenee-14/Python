'''
2024.2.29
11728 - 배열 합치기
'''

n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

num = a + b
num.sort()

print(*num, sep=" ")
