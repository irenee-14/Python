'''
2024.3.23
5357 - Dedupe
'''
n = int(input())
for _ in range(n):
    s = input()
    prev = ''
    for i in range(len(s)):
        if prev != s[i]:
            print(s[i], end="")
            prev = s[i]
    print()
