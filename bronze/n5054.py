''''
2025.6.20
5054 - 주차의 신
'''

t = int(input())

for _ in range(t):
    n = int(input())
    parking = sorted(map(int, input().split()))
    print((parking[-1] - parking[0]) * 2)