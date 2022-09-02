'''
1546 - 평균
2022.9.2
'''

n = int(input())
score = list(map(int, input().split()))
max_score = max(score)

result = 0
for var in score:
    result += (var/max_score * 100)
print(result/n)