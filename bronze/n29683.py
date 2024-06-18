'''
2024.6.18
29683 - 크리스마스 복권(Рождественская лотерея)
'''

n, A = map(int, input().split())
a = list(map(int, input().split()))

res =  0

for i in range(n):
    res += a[i] // A
print(res)
