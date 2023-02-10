'''
2023.1.24
1992 - 쿼드트리 - 분할정복
'''
n = int(input())
tree = [list(map(int, input().rstrip())) for _ in range(n)]

def quad(x, y, n):
    for i in range(x, x + n):
        for j in range(y, y + n):
            if tree[x][y] != tree[i][j]:
                print("(", end="")
                
                quad(x, y, n // 2)
                quad(x, y + n // 2, n // 2)
                quad(x + n // 2, y, n // 2)
                quad(x + n // 2, y + n // 2, n // 2)
                
                print(")", end="")
                return

    if tree[x][y] == 1:
        print(1, end="")
    else:
        print(0, end="")

quad(0, 0, n)
