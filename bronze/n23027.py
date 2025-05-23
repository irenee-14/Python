'''
2025.5.23
23027 - 1번부터 문제의 상태가…?
'''

S = list(input())

if 'A' in S:
    for i in range(len(S)):
        if S[i] == 'B' or S[i] == 'C' or S[i] == 'D' or S[i] == 'F':
            S[i] = 'A'
elif 'B' in S:
    for i in range(len(S)):
        if S[i] == 'C' or S[i] == 'D' or S[i] == 'F':
            S[i] = 'B'
elif 'C' in S:
    for i in range(len(S)):
        if S[i] == 'D' or S[i] == 'F':
            S[i] = 'C'
else:
    for i in range(len(S)):
        S[i] = 'A'

print(*S, sep="")