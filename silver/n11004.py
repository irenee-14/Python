'''
2023.4.27
11004 - K번째 수
'''

n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
print(a[k - 1])