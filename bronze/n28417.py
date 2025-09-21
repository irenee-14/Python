'''
2025.9.21
28417 - 스케이트 보드
'''

N = int(input())
res = 0

for _ in range(N):
    Skateboard = list(map(int, input().split()))
    Run = Skateboard[:2]
    Trick = Skateboard[2:]

    Run.sort(reverse=True)
    Trick.sort(reverse=True)

    result = max(res, Run[0] + sum(Trick[:2]))

print(res)