'''
2024.10.20
2997 - 네 번째 수
'''

a = list(map(int, input().split()))
a.sort()
if a[1] - a[0] == a[2] - a[1]:
    print(a[2] * 2 - a[1])
elif a[1] - a[0] > a[2] - a[1]:
    print(a[1] * 2 - a[2])
else:
    print(a[1] * 2 - a[0])