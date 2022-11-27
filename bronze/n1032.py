'''
2022.11.27
1032 - 명령 프롬프트
'''

n = int(input())
raw = list(input())

for i in range(n-1):
    b = list(input())
    for j in range(len(raw)):
        if raw[j] != b[j]:
            raw[j] = '?'
print(*raw,sep="")