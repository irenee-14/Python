'''
2025.7.30
5612 - 터널의 입구와 출구
'''

n = int(input())
tmp = list()

tmp.append(int(input()))
for i in range(n):
    a, b = map(int, input().split())
    tmp.append(tmp[i] + a - b)

for i in range(n + 1):
    if tmp[i] < 0:
        print(0)
        exit()
print(max(tmp))