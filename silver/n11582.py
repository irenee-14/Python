'''
2025.7.22
11582 - 치킨 TOP N
'''

N = int(input())
chicken = list(map(int, input().split()))
k = int(input())

index = N // k
arr = []

for i in range(0, N, index):
    arr = chicken[i:i+index]
    arr.sort()
    for j in arr:
        print(j, end=' ')
