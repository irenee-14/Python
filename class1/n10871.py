'''산
2022.9.13
10871 - X보다 작은 수
'''

n, x = map(int, input().split())
n_list = list(map(int, input().split()))

for i in range(n):
    if n_list[i] < x:
        print(n_list[i], end=" ")

