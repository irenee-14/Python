'''
2024.10.18
1912 - 연속합
'''

n = int(input())
m = list(map(int, input().split()))

for i in range(1, n):
    m[i] = max(m[i], m[i] + m[i - 1])
print(max(m))