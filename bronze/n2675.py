'''
2025.8.6
2675 - 문자열 반복
'''

n = int(input())

for _ in range(n):
    cnt, word = input().split()
    for x in word:
        print(x * int(cnt), end='')
    print()