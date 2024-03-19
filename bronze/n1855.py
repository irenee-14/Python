'''
2024.3.19
1855 - 암호
'''

n = int(input())
s = input()
row = len(s) // n

arr = [[] for _ in range(n)]

for i in range(1, row + 1):
    if i % 2 == 1:
        for j in range(n):
            arr[j].append(s[j])
        s = s[n:]
    else:
        for j in range(n):
            arr[j].append(s[n - j - 1])
        s = s[n:]
res = ''
for i in arr:
    for j in i:
        res += j
print(res)