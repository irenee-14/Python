'''
2024.11.28
19942 - 다이어트
'''


def recur(idx, A, B, C, D, E):
    global answer
    global used
    global answer_used

    if a <= A and b <= B and c <= C and d <= D: # 모든 필요 영양소를 충족
        if answer > E:
            answer = E
            answer_used = []
            for i in used:
                answer_used.append(i)

    if idx == N:
        return

    used.append(idx + 1)
    # 사용한 경우
    recur(idx + 1, A + ingre[idx][0] , B + ingre[idx][1], C + ingre[idx][2], D + ingre[idx][3], E + ingre[idx][4])
    used.pop()
    # 사용하지 않은 경우
    recur(idx + 1, A, B, C, D, E)


N = int(input())
a, b, c, d = map(int, input().split())
ingre = [list(map(int, input().split())) for _ in range(N)]

answer = 9999999999
used = []
answer_used = []

recur(0, 0, 0, 0, 0, 0)

answer_used.sort()
if answer_used:
    print(answer)
    print(*answer_used)
else:
    print(-1)