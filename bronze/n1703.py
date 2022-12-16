'''
2022.12.16
1703 - 생장점
'''

while 1:
    li = list(map(int, input().split()))
    if li[0] == 0:
        break
    n = 1
    for i in range(li[0]):
        sf = li[2*i + 1]
        p = li[2*i + 2]
        n = n*sf - p
    print(n)