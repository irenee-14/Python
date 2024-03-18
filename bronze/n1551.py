'''
2024.3.18
1551 - 수열의 변화
'''
N, K = map(int, input().split())
arr = list(map(int, input().split(',')))
for _ in range(K):
    tmp = [arr[i+1] - arr[i] for i in range(len(arr)-1)]
    arr = tmp
print(*arr, sep=',')