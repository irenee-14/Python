'''
2023.3.5
2587 - 대표값  2
'''
nums = []

for _ in range(5):
    nums.append(int(input()))
nums.sort()
print(int(sum(nums)/5))
print(nums[2])
