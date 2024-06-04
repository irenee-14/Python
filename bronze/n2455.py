'''
2024.6.4
2455 - 지능형 기차
'''
arr = []
result = 0

for i in range(4):
    a, b = map(int, input().split())

    result = result - a + b
    arr.append(result)

print(max(arr))