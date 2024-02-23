'''
2024.2.23
15652 - N과 M (4)
'''
n, m = map(int, input().split())

num = []

def nm(start):
    if len(num) == m:
        print(*num, sep=' ')
        return
    
    for i in range(start, n + 1):
        num.append(i)
        nm(i)
        num.pop()
    
nm(1)
