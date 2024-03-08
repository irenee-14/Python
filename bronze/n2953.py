'''
2024.3.8
2953 - 나는 요리사다
'''

res = []
for _ in range(5):
    score = list(map(int, input().split()))
    res.append(sum(score))
print(res.index(max(res)) + 1, max(res))