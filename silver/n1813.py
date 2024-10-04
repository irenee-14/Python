'''
2024.10.4
1813 - 논리학 교수
'''

n = int(input())
nums = list(map(int, input().split()))

res = -1

for i in range(n + 1):
    true = nums.count(i)

    if true == i:
        res = max(res, i)
print(res)