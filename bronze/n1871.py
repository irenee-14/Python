'''
2024.10.29
1871 - 좋은 자동차 번호판
'''

n = int(input())
for i in range(n):
    al, num = input().split('-')
    num = int(num)
    res = 0
    for j in range(3):
        res += (ord(al[j]) - 65) * 26 ** (2 - j)
    print("nice" if abs(res - num) <= 100 else "not nice")
