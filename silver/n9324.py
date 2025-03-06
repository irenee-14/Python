'''
2025.3.6
9324 - 진짜 메시지
'''

T = int(input())

for i in range(T):
    M = list(input())
    msg = 'OK'
    check = [0] * 26
    for j in range(len(M)):
        tmp = ord(M[j]) - ord('A')

        check[tmp] += 1
        if check[tmp] % 3 == 0:
            if (j < len(M) - 1 and M[j] != M[j + 1]) or j == len(M) - 1:
                msg = 'FAKE'
                break
        elif check[tmp] % 4 == 0:
            check[tmp] = 0
    print(msg)
