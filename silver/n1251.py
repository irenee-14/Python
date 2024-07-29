'''
2024.7.29
1251 - 단어 나누기
'''

s = input()
res = []

for i in range(1, len(s)):
    for j in range(i + 1, len(s)):
        a = s[:i][::-1]
        b = s[i:j][::-1]
        c = s[j:][::-1]
        res.append(a + b + c)
res.sort()
print(res[0])