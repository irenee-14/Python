'''
2023.4.26
2669 - 직사각형 네개의 합집합의 면적 구하기
'''
board = [[0 for _ in range(101)] for _ in range(101)]
res = 0 

for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    
    for i in range(x1, x2):
        for j in range(y1, y2):
            board[i][j] = 1 

for i in board:
    res += sum(i)
print(res)
