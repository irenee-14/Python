'''
2022.12.22 
1951 - 활자
'''
n = int(input())
tmp = [0 for i in range(10)]
count = 1

while n != 0:
    while n % 10 != 9:
        for i in str(n):
            tmp[int(i)] += count
        n -= 1
    if n < 10:
        for i in range(n + 1):
            tmp[i] += count
        tmp[0] -= count
        break
    else:
        for i in range(10):
            tmp[i] += (n // 10 + 1) * count
    tmp[0] -= count
    count *= 10
    n //= 10

print(sum(tmp) % 1234567)
