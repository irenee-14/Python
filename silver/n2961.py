'''
2024.11.27
2961 - 도영이가 만든 맛있는 음식
'''

# 완전 탐색적 사고
# 재료를 1부터 N까지 다 써보면 되겠네!


def recur(idx, S, B, use):
    global answer

    if idx == N:
        if use == 0:
            return
        result = abs(S - B)
        answer = min(answer, result)
        return

    # 사용한 경우
    recur(idx + 1, S * ingre[idx][0], B + ingre[idx][1], use + 1)
    # 사용하지 않은 경우
    recur(idx + 1, S, B, use)

N = int(input())
ingre = [list(map(int, input().split())) for _ in range(N)]

answer = 9999999999
recur(0, 1, 0, 0)
print(answer)