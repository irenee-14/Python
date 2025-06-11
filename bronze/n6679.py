'''
2025.6.11
6679 - 싱기한 네자리 숫자
'''


def convert(n, k):
    ans = 0
    while n > 0:
        ans += n % k
        n = n // k
    return ans


for i in range(1000, 10000):
    ten = convert(i, 10)
    twe = convert(i, 12)
    six = convert(i, 16)
    if ten == twe and twe == six: print(i)