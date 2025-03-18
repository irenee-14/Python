'''
2025.3.18
10876 - 중복 빼고 정렬하기
'''

n = int(input())
nums = set(list(map(int, input().split())))
nums = list(nums)
nums.sort()
print(*nums)