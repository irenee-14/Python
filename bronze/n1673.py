'''
2024.9.3
1673 - 치킨 쿠폰
'''

while True:
    try:
        n, k = map(int, input().split())
        res = 0
        res += n
        while n // k:
            res += n // k
            n = n // k + n % k
        print(res)
    except:
        break
