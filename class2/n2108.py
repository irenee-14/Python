'''
2022.10.7
2108 - 통계학
'''

from collections import Counter

import sys
input = sys.stdin.readline

n = int(input())
nums = []
n_sum = 0

for i in range(n):
    nums.append(int(input()))
    n_sum += nums[i]
nums.sort()

  # Counter : 각 요소의 개수를 나타내줌
  # Counter(nums). => Counter({-2: 2, -1: 2, -3: 1})
  # -2 : 2개, -2 : 2개, -3 : 1개
  # most_common : 데이터가 많은 순으로 정렬해서 리턴
  # 숫자를 쓰면 몇개까지 리턴할지
cnt = Counter(nums).most_common(2)

# 평균
print(round(n_sum/n))
# 중앙값
print(nums[n//2])
# 최빈값
if len(nums) > 1:
    # 최빈값이 1개가 아닐 경우
    # 빈도수가 같을 경우
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
# 범위
print(max(nums)-min(nums))
