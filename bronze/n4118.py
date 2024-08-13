'''
2024.8.13
4118 - Fred's Lotto Tickets
'''

while True:
    n = int(input())
    if n == 0:
        break
    board = [0] * 49
    for i in range(n):
        lotto = list(map(int, input().split()))
        for x in lotto:
            board[x - 1] = 1
    if sum(board) == 49:
        print('Yes')
    else:
        print('No')
