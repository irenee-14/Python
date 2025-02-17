'''
2025.2.17
21312 - 홀짝 칵테일
'''

nums = list(map(int,input().split()))
odd = []

for i in range(3):
    if nums[i] % 2 != 0:
        odd.append(nums[i])
res = 1
if not odd:
    for i in range(3):
        res *= nums[i]

else:
    for i in range(len(odd)):
        res *= odd[i]
print(res)