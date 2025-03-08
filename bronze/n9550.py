'''
2025.3.8
9550 - 아이들은 사탕을 좋아해
'''

for _ in range(int(input())):
    N, K = map(int, input().split())
    candy = list(map(int, input().split()))
    answer = 0

    for i in candy:
        answer += i // K
    print(answer)