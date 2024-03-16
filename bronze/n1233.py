'''
2024.3.16
1233 - 주사위
'''
# s1 20, s2 20, s3 40 -> 총 80
s1, s2, s3 = map(int, input().split())
res = [0] * 81

for i in range(1, s1 + 1):
    for j in range(1, s2 + 1):
        for k in range(1, s3 + 1):
            res[i + j + k] += 1
print(res.index(max(res)))