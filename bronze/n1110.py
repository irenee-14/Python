'''
2023.1.15
1110 - 더하기 사이클
'''

n = int(input())
num = n
count = 0

while True:
    a = num // 10
    b = num % 10
    c = (a + b) % 10
    num = (b * 10) + c
    count += 1
    if (num == n):
        break

print(count)