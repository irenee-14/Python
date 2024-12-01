'''
2024.12.1
25305 - 커트라인
'''

n, k = map(int, input().split())
score = list(map(int, input().split()))
score.sort(reverse=True)

score = score[:k]
print(score[-1])