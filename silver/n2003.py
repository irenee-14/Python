'''
2023.3.13
2003 - 수들의 합 2
'''

# n, m = map(int, input().split())
# nums = list(map(int, input().split()))
# cnt = 0
#
# for i in range(n):
#     tmp = 0
#     for j in range(i, n):
#         tmp += nums[j]
#         if tmp == m:
#             cnt += 1
#             break
#         elif tmp > m:
#             break
# print(cnt)

n, m = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0
low, high = 0, 1
tmp = nums[low]

while low < n:
    if tmp == m:
        cnt += 1
        tmp -= nums[low]
        low += 1

    if high == n and tmp < m:
        break
    elif tmp < m:
        tmp += nums[high]
        high += 1
    elif tmp > m:
        tmp -= nums[low]
        low += 1
print(cnt)