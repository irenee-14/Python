'''
2024.11.5
10815 - 숫자 카드
'''

n = int(input())
n_nums = sorted(list(map(int, input().split())))
m = int(input())
m_nums = list(map(int, input().split()))

''' dic '''
# dic = {}
# for i in range(n):
#     dic[n_nums[i]] = 0
#
# res = []
#
# for x in m_nums:
#     if x not in dic:
#         res.append(0)
#     else:
#         res.append(1)
# print(*res, sep=' ')

''' 이분탐색 '''

for x in m_nums:
    low, high = 0, n - 1
    flag = False
    while low <= high:
        mid = (low + high) // 2
        if n_nums[mid] > x:
            high = mid - 1
        elif n_nums[mid] < x:
            low = mid + 1
        else:
            flag = True
            break
    print(1 if flag else 0, end=' ')
