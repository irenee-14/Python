'''
2023.2.14
10156 - 과자
'''

k, n, m= map(int, input().split())
answer = k * n - m

if answer > 0:
    print(answer)
else:
    print(0)
