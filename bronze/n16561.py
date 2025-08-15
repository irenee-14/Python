'''
2025.8.15
16561 - 3의 배수
'''

n = int(input())
num = 1
cnt = 2

for i in range(9, n, 3):
    num += cnt
    cnt += 1
print(num)