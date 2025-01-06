'''
2025.1.6
5355 - 화성 수학
'''

case = int(input())

for _ in range(case):
    mars = list(map(str, input().split()))
    answer = float(mars[0])
    for i in range(1, len(mars)):
        if mars[i] == "#":
            answer -= 7
        elif mars[i] == "%":
            answer += 5
        elif mars[i] == "@":
            answer *= 3

    print("%0.2f" % answer)