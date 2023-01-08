'''
2023.1.8
1543 - 문서 검색
'''

a = input()
b = input()
count = 0
n = 0

while n <= len(a) - len(b):
    if a[n:n + len(b)] == b:
        count += 1
        n += len(b)
    else:
        n += 1
print(count)
