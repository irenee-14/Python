'''
2024.5.21
1120 - 문자열
'''

a, b = map(str, input().split())

res = []
for i in range(len(b) - len(a) + 1):
    count = 0
    for j in range(len(a)):
        if a[j] != b[i + j]:
            count += 1
    res.append(count)

print(min(res))