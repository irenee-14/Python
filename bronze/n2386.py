'''
2024.6.8
2386 - 도비의 영어 공부
'''

while True:
    S = list(map(str, input().split()))
    find = S[0]
    target = S[1:]
    if find == '#':
        break
    print(find, str(target).lower().count(find))