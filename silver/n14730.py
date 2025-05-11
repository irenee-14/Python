'''
2025.5.11
14730 - 謎紛芥索紀 (Small)
'''

n = int(input())
res = 0
for i in range(n):
    c, k = map(int, input().split())
    res += c * k
print(res)