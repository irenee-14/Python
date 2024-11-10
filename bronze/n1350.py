'''
2024.11.10
1350 - 진짜 공간
'''

n = int(input())
file = map(int, input().split())
cluster = int(input())

res = 0
for i in file:
    if i % cluster > 0:
        res += i // cluster + 1
    else:
        res += i // cluster
print(cluster * res)