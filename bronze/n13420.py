'''
2025.6.14
13420 - 사칙연산
'''

T = int(input())
for _ in range(T):
    prob, answer = map(str, input().split('='))

    if eval(prob) == int(answer):
        print("correct")
    else:
        print("wrong answer")