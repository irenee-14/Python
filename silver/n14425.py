'''
2024.12.10
14425 - 문자열 집합
'''

n, m = map(int, input().split())
s = [input() for _ in range(n)]
cnt = 0

for i in range(m):
    if input() in s:
        cnt += 1
print(cnt)

