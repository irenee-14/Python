'''
2024.4.17
10973 - 이전순열
'''
n = int(input())
arr = list(map(int, input().split()))

k = -1 

for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        k = i 
if k == -1:
    print(-1)
else:
    for i in range(k + 1, len(arr)):
        if arr[i] < arr[k]:
            m = i
    tmp = arr[k]
    arr[k] = arr[m]
    arr[m] = tmp
    
    tmp = arr[k + 1 :]
    tmp.sort(reverse=True)
    res = arr[:k + 1] + tmp 

    print(*res, end="")
