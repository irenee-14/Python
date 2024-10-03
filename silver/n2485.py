'''
2024.10.3
2485 - 가로수
'''

def cal_gcd(a, b):
    while b > 0:
        tmp = a
        a = b
        b = tmp % b
    return a

n = int(input())
tree = [int(input()) for _ in range(n)]

sep = []

for i in range(n - 1):
    sep.append(tree[i + 1] - tree[i])

gcd = sep[0]
for i in range(1, len(sep)):
    gcd = cal_gcd(gcd, sep[i])

cnt = 0
for i in sep:
    cnt += i // gcd - 1
print(cnt)