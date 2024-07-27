'''
2024.7.27
4107 - Knitting
'''


while True:
    n, m, k = map(int, input().split())
    if n == 0 or m == 0 or k == 0:
        break

    res = 0
    cur = n
    stitch = list(map(int, input().split()))
    for i in range(m):
        res += n
        n += stitch[i % k]

    print(res)
