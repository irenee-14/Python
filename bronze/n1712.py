'''
2023.2.10
1712 - 손익분기점
'''
a, b, c = map(int, input().split())

if b >= c:
    print(-1)
else:
    print(int(a/(c-b)+1))
