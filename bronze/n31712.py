'''
2024.10.8
31712 - 핑크빈 레이드
'''

C = []
D = []
for i in range(3):
    c, d = list(map(int, input().split()))
    C.append(c)
    D.append(d)
H = int(input())

sec = -1
while H > 0:
    sec += 1
    for i in range(3):
        if sec % C[i] == 0:
            H -= D[i]


print(sec)
