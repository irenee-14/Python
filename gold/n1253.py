'''
2024.2.3
1253 - 좋다
'''
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.sort()

cnt = 0
for i in range(n):
    res = nums[i]
    start = 0
    end = len(nums) - 1
    
    while start < end:
        if nums[start] + nums[end] == res:
            if start == i:
                start += 1 
            elif end == i:
                end -= 1 
            else:
                cnt += 1 
                break 
        elif nums[start] + nums[end] > res:
            end -= 1
        elif nums[start] + nums[end] < res:
            start += 1
print(cnt)

# 4
# 0 0 0 3
# 6
# 1 2 2 4 4 6
# 5
# 1 2 3 4 5
