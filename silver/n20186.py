'''
2022.12.23
20186 - 수 고르기
'''

n, k = map(int, input().split())
nums = sorted(list(map(int, input().split())))
n_sum = 0
for i in range(1, k+1):
    n_sum += nums[-i]-i+1
print(n_sum)