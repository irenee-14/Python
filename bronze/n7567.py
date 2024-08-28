'''
2024.8.28
7567 - 그릇
'''

s = list(str(input()))
res = 10

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        res += 5
    else:
        res += 10
print(res)

