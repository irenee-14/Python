'''
2023.3.21
9093 - 단어 뒤집기
'''
n = int(input())

for _ in range(n):
    s = input().split()
    for word in s:
        print(word[::-1], end=' ')
