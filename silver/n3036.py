'''
2023.4.21
3036 - 링
'''

def gdc(a, b):
    while (b != 0):
        n = a % b
        a = b
        b = n
    return a

n = int(input())
nums = list(map(int, input().split()))
for i in range(1, n):
    res = gdc(nums[0], nums[i])
    print('{0}/{1}'.format(nums[0]//res, nums[i]//res))