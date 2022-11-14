'''
2022.11.14
1074 - Z
'''
import sys
input = sys.stdin.readline

def visited(n, x, y):
    global res
    
    if x == r and y == c:
        print(int(res))
        exit(0)
    if x > r or x + n <= r or y > c or y + n <= c:
        res += n*n
        return
    
    # 1/2/3/4사분면을 재귀적으로 탐색
    visited(n/2, x, y) # 1사분면
    visited(n/2, x, y + n/2) # 2사분면
    visited(n/2, x + n/2, y) # 3사분면
    visited(n/2, x + n/2, y + n/2) # 4사분면
    


N, r, c = map(int, input().split())
res = 0
visited(2**N, 0, 0)
