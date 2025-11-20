'''
2025.11.20
11094 - 꿍 가라사대
'''

N = int(input())

for _ in range(N):
    s = list(map(str, input().split()))

    if s[0] == 'Simon' and s[1] == 'says':
        print("", " ".join(map(str, s[2:])))
    else:
        continue