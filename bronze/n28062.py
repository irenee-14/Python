'''
2025.9.30
28062 - 준석이의 사탕 사기
'''

N = int(input())
candy = list(map(int, input().split()))
result = 0
tmp = []

for i in candy:
    if i % 2 == 1:  # 홀수 사탕이 들어있는 사탕 묶음
        tmp.append(i)
    else:
        result += i

if len(tmp) % 2 == 1:
    tmp.sort(reverse=True)
    del tmp[-1]
    result += sum(tmp)
else:
    result += sum(tmp)

print(result)