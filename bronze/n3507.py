'''
2022.12.18
3507 - Automated Telephone Exchange
'''
n = int(input())
cnt = 0
if n <= 198:
    for i in range(1, 100):
        for j in range(1, 100):
            if i+j == n:
                cnt += 1
print(cnt)