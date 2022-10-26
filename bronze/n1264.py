'''
2022.10.27
1264 - 모음의 개수
'''
while True:
    s = input()
    if s == '#':
        break
    cnt = 0
    for c in s:
        if c in 'aeiouAEIOU':
            cnt += 1
    print(cnt)
