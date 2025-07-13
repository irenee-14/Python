'''
2025.7.13
16504 - 종이접기
'''

res = 0
for _ in range(int(input())):
    res += sum(list(map(int, input().split())))
print(res)