'''
2024.11.8
2503 - 숫자야구
'''

n = int(input())
numbers = [list(map(int, input().split())) for _ in range(n)]
answer = 0

# 세 자리 숫자 만들기
for a in range(1, 10):  # 100의 자리수
    for b in range(1, 10):  # 10의 자리수
        for c in range(1, 10):  # 1의 자리수
            counter = 0

            # (2) 다른 세 자리수
            if a == b or b == c or c == a:
                continue

            # (3) 배열에 넣은 조건을 넣어주기
            for array in numbers:
                check = list(str(array[0]))  # ['1','2','3']
                strike = array[1]
                ball = array[2]

                strike_count = 0
                ball_count = 0
                num = [str(a), str(b), str(c)]

                for i in range(3):
                    if check[i] == num[i]:
                        strike_count += 1
                    elif num[i] in check:
                        ball_count += 1

                if strike == strike_count and ball == ball_count:
                    counter += 1

            if counter == n:
                answer += 1

print(answer)
