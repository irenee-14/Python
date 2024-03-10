'''
2024.3.10
1284 - 집주소
'''
while True:
    n = input()
    if n == '0':
        break
    cnt = len(n) + 1
    for x in n:
        if x == '0':
            cnt += 4
        elif x == '1':
            cnt += 2
        else:
            cnt += 3
    print(cnt)


