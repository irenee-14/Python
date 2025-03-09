'''
2025.3.9
25418 - 정수 a를 k로 만들기
'''

a, k = map(int, input().split())
c = 0
while a <= k // 2:
    c += 1 + (k & 1)
    k = k//2
print(c + k - a)
