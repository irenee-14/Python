'''
2025.5.14
20053 - 최소, 최대 2
'''

t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(min(arr),max(arr))