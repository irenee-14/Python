'''
2022.12.25
1526 - 가장 큰 금민수
'''

N = int(input())

while True:
    f = True
    for i in str(N):
        if i != '4' and i != '7':
            f = False
            N -= 1
    if f:
        print(N)
        break
