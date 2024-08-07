'''
2024.8.7
3273 - 두 수의 합
'''

n = int(input())
a = list(map(int, input().split()))
x = int(input())

a.sort()
left, right = 0, n - 1
res = 0
while left < right:
    tmp = a[left] + a[right]
    if tmp == x:
        res += 1
        left += 1
    elif tmp < x:
        left += 1
    else:
        right -= 1
print(res)