'''
2025.4.10
17614 - 369
'''

n = int(input())
cnt = 0
for num in range(1, n + 1):
    for i in str(num):
        if i == '3' or i == '6' or i == '9':
            cnt += 1
print(cnt)
