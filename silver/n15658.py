'''
2024.4.22 
15658 - 연산자 끼워넣기 (2)
'''
N = int(input())
A = list(map(int, input().split()))
ops = list(map(int, input().split()))

max_res = -1000000000
min_res = 1000000000

def dfs(index, res):
    global max_res, min_res
    
    if index == N:
        max_res = max(max_res, res)
        min_res = min(min_res, res)
        return 
    
    if ops[0] > 0:
        ops[0] -= 1
        dfs(index + 1, res + A[index])
        ops[0] += 1 
    if ops[1] > 0:
        ops[1] -= 1
        dfs(index + 1, res - A[index])
        ops[1] += 1 
    if ops[2] > 0:
        ops[2] -= 1
        dfs(index + 1, res * A[index])
        ops[2] += 1 
    if ops[3] > 0:
        ops[3] -= 1
        dfs(index + 1, int(res / A[index]))
        ops[3] += 1 
        
dfs(1, A[0])
print(max_res, min_res, sep="\n")
