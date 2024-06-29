'''
2024.6.29
10039 - 평균 점수
'''
res = 0
for _ in range(5):
    tmp = int(input())
    if tmp < 40:
        res += 40
    else:
        res += tmp
print(res//5)