'''
2023.1.22
10797 - 10부제
'''

n = int(input())
car = list(map(int, input().split()))

cnt = 0

for i in car:
    if i == n:
        cnt += 1
print(cnt)
