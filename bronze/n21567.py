'''
2025.4.5
21567 - 숫자의 개수 2
'''

cnt = [0] * 10
total = 1

for i in range(3):
    total *= int(input())

for j in str(total):
    cnt[int(j)] += 1

for n in cnt:
    print(n)
