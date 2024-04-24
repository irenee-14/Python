'''
2024.4.24
1292 - 쉽게 푸는 문제
'''

a, b = map(int,input().split())
data = [0]
res = 0

for i in range(1, b + 1):
    for j in range(i):
        data.append(i)

for i in range(a, b + 1):
  res += data[i]

print(res)