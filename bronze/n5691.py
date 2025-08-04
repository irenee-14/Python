'''
2025.8.4
5691 - 평균 중앙값 문제
'''

while True :
    a, b = map(int, input().split())
    if a == b == 0:
        break
    print(2 * a - b)