'''
2025.1.11
10987 - 모음의 개수
'''

ans = 0
for c in input():
    if c in ['a', 'e', 'i', 'o', 'u']:
        ans += 1
print(ans)