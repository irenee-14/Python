'''
2025.6.25
4998 - 저금
'''

try:
    while True:
        n, b, m = map(float, input().split())
        cnt = 0
        while n < m:
            n += n * (b / 100)
            cnt += 1
        print(cnt)

except:
    exit()
