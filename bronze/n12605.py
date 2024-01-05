'''
2023.4.1
12605 - 단어 순서 뒤집기
'''

n = int(input())

for i in range(n):
    case = list(input().split())
    print("Case #", i + 1, ": ", sep="", end="")
    print(*case[::-1])