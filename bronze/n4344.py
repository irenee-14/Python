'''
2023.2.7
4344 - 평균은 넘겠지
'''

n = int(input())

for _ in range(n):
    count = 0
    nums = list(map(int, input().split()))
    av = sum(nums[1:]) / nums[0]
    for i in nums[1:]:
        if i > av:
            count += 1
    print("{:.3f}".format(count / nums[0] * 100), '%', sep="")