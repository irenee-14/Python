'''
2025.4.23
2992 - 크면서 작은 수
'''

X = list(input())
n = int("".join(X))

flag = 0
for i in range(n + 1, 999999):
    if sorted(X) == sorted(list(str(i))):
        flag = i
        break
print(flag)

