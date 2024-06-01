'''
2024.6.1
2576 - 홀수
'''

nums = [int(input()) for _ in range(7)]
odd = []
for x in nums:
    if x % 2:
        odd.append(x)
if len(odd):
    print(sum(odd))
    print(min(odd))
else:
    print(-1)