'''
2023.1.27
2667 - 단지 번호 붙이기
'''
n = int(input())
board = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if board[x][y] == 1:
        global home_count
        home_count += 1
        board[x][y] = 0
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False


home_count = 0
num = []

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            num.append(home_count)
            home_count = 0 

num.sort()
print(len(num))
print(*num, sep="\n")
    
