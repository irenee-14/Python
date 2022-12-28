'''
2022.12.28
2845 - 파티가 끝나고 난 뒤
'''
a, b = map(int, input().split())
people = list(map(int, input().split()))
party = a * b
for i in people:
    print(i - party, end=' ')
