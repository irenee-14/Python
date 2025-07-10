'''
2025.7.10
29752 - 최장 스트릭
'''

lst = list(map(int, input().split()))

res = 0
max_res = 0
for i in lst:
    if i == 0:
        res = 0
        continue
    res += 1
    max_res = max(res, max_res)
print(max_res)