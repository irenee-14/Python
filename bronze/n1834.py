'''
2025.2.5
1834 - 나머지와 몫이 같은 수
'''

n = int(input())
res = 0
for i in range(1, n):
    res += n * i + i
print(res)

