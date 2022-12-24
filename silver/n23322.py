'''
2022.12.24
23322 - 초콜릿 뺏어 먹기
'''

n, k = map(int, input().split())
cho = sorted(list(map(int, input().split())))

eat = 0
cnt = 0

min_cho = min(cho)
for i in range(1, len(cho)):
    if cho[i-1] <= cho[i] and min_cho < cho[i]:
        while cho[i] > cho[i-1]:
            cho[i] -= 1
            cnt += 1
        eat += 1
print(cnt, eat)
