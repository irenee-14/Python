'''
2022.11.16
18698 - The Walking Adam
'''
n = int(input())

for _ in range(n):
    walk = input()
    cnt = 0
    for i in walk:
        if i == 'U':
            cnt += 1
        else:
            break
    print(cnt)
