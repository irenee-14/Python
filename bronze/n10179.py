'''
2023.2.9
10179 - 쿠폰
'''

n = int(input())

for _ in range(n):
    a = float(input()) * 0.8
    print("${:.2f}".format(a))
