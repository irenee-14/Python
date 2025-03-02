'''
2025.3.2
17202 - 핸드폰 번호 궁합
'''

x = list(input())
y = list(input())
tmp = []
answer = ''

for i in range(8):
    answer += x[i] + y[i]

while len(answer) != 2:
    for i in range(len(answer) - 1):
        tmp.append(str((int(answer[i]) + int(answer[i + 1])) % 10))
    answer = ''.join(tmp)
    tmp = []

print(answer)
