'''
2023.4.9
27110 - 특식 배부
'''
N = int(input())
food = list(map(int, input().split()))
res = 0

for i in range(3):
    if food[i] <= N :
        res += food[i]
    else:
        res += N

print(res)
