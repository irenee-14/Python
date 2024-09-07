'''
2024.9.7
1864 - 문어 숫자
'''

nums = {'-':0, '\\':1, '(':2, '@':3, '?':4, '>':5, '&':6, '%':7, '/':-1}
while True:
    n = input()
    if n == '#':
        break
    res = 0
    for i in range(len(n)):
        res += nums[n[i]] * 8 ** (len(n) - i - 1)
    print(res)