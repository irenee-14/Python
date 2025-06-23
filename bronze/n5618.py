'''
2025.6.23
5618 - 공약수
'''

n = int(input())
numberList = list(map(int, input().split()))

minNum = min(numberList)

for i in range(1, minNum + 1):
    cnt = 0
    for num in numberList:
        if num % i == 0:
            cnt += 1
        else:
            break
    if cnt == n:
        print(i)
