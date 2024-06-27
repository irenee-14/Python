'''
2024.6.27
1453 - 피씨방 알바
'''

n = int(input())
customer = list(map(int, input().split()))
cnt = 0
seat = []
for i in range(n):
    if customer[i] in seat:
        cnt += 1
    else:
        seat.append(customer[i])
print(cnt)