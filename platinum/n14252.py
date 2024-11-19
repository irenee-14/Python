'''
2024.11.19
14252 - 공약수열
2.2 - n5
'''

# 완전탐색
# 정수론

# 두 수를 비교해서 최대 공약수가 1이라면 OK
# 두 수를 비교해서 최대 공약수가 1이 아니라면 NOK

# 숫자를 하나 추가하거나
# 또는 두 개 추가한다.

# 42부터 2184까지 하나씩 숫자를 올려가면서 확인

# for i in range(42, 2184):
#     if gcd(42, i) == 1:
#         if gcd(2184, i) == 1:
#             count += 1
#             break
#
# for i in range(2184, 2200):
#     if gcd(42, i) == 1:
#         if gcd(2184, i) == 1:
#             count += 1
#             break
#     if i == 2199:
#         count += 2

def _gcd(a, b):
    while a % b != 0:
        tmp = a % b
        a = b
        b = tmp
    return b

N = int(input())
nums = list(map(int, input().split()))
nums.sort()
count = 0

for i in range(0, N - 1):
    a = nums[i]
    b = nums[i + 1]
    for j in range(a, b):
        if _gcd(a, b) == 1:
            continue
        elif _gcd(a, j) == 1:
            if _gcd(b, j) == 1:
                count += 1
                break
        elif j == b - 1:
            count += 2
print(count)