'''
2025.1.1
19532 - 수학은 비대면강의입니다
'''

a, b, c, d, e, f = map(int, input().split())
x = ((e * c) - (b * f)) // ((a * e) - (d * b))
y = ((a * f) - (d * c)) // ((a * e) - (d * b))
print(x, y)
