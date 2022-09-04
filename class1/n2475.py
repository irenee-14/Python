'''
2475 - 검증 수
2022.9.5
'''

num = list(map(int, input().split()))
only = 0
for i in num:
    only += i*i
print(only % 10)
