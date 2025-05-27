'''
2025.5.27
14659 - 한조서열정리하고옴ㅋㅋ
'''

n = int(input())
arr = list(map(int, input().split()))

high = 0
cnt = 0
total = []

for i in arr:
    if i > high:
        high = i
        cnt = 0
    else:
        cnt += 1
    total.append(cnt)

print(max(total))