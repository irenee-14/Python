'''
2023.1.31
4673 - 셀프 넘버
'''

nums = set(range(1, 10001))
res = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    res.add(i)

self_num = sorted(nums - res)
print(*self_num, sep="\n")