'''
2025.4.10
17614 - 369
'''

N = int(input())
check = '369'
res = 0
for i in range(1, N+1):
    str_num = str(i)
    for c in check:
        res += str_num.count(c)
print(res)
