'''
2025.7.10
29752 - 최장 스트릭
'''

N = int(input())
A = list(input().split())

result = 0
tmp = 0

for i in A:
    if i != '0':
        tmp += 1
        result = max(result, tmp)

    if i == '0':
        result = max(result, tmp)
        tmp = 0
print(result)
