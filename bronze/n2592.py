'''
2025.1.9
2592 - 대표값
'''

count = [0] * (1000 + 1)

res = 0
for _ in range(10):
    num = int(input())
    res += num
    count[num] += 1

print(res // 10)  # 최대값
print(count.index(max(count)))  # 최빈값
