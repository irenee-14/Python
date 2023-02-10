'''
2023.2.3 
14888 - 연산자 끼워넣기 - dfs
'''
n = int(input())
a = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

res_max = -1e9
res_min = 1e9


def dfs(i, arr):
    global add, sub, mul, div, res_max, res_min
    
    if i == n:
        res_max = max(res_max, arr)
        res_min = min(res_min, arr)
    else:
        if add > 0:
            add -= 1 
            dfs(i + 1, arr + a[i])
            add += 1 
        if sub > 0:
            sub -= 1 
            dfs(i + 1, arr - a[i])
            sub += 1
        if mul > 0:
            mul -= 1 
            dfs(i + 1, arr * a[i])
            mul += 1 
        if div > 0:
            div -= 1 
            dfs(i + 1, int(arr / a[i]))
            div += 1


dfs(1, a[0])
print(res_max, res_min, sep="\n")
