'''
2024.8.27
2535 - 아시아 정보 올림피아드
'''

n = int(input())
lst = []

for i in range(n):
    lst.append(list(map(int, input().split())))

lst.sort(key=lambda x:-x[-1])
print(*lst[0][:2])
print(*lst[1][:2])

i = 2
if lst[0][0] == lst[1][0]:
    while lst[0][0] == lst[i][0]:
        i += 1
print(*lst[i][:2])