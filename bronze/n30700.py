'''
2025.11.4
30700 - KOREA 문자열 만들기
'''

S = input()
korea = ["K", "O", "R", "E", "A"]
length = 0
for i in range(len(S)):
    if S[i] == korea[length % 5]:
        length += 1
print(length)
