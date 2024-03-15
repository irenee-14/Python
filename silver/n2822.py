'''
2024.3.13
2822 - 점수계산
'''
score = []
for i in range(8):
    score.append(int(input()))

select = []
res = 0

for i in range(5):
    res += max(score)
    select.append(score.index(max(score)) + 1)
    score[score.index(max(score))] = -1

select.sort()

print(res)
print(*select)
