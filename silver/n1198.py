'''
2024.4.6
1198 - 삼각형으로 자르기
'''
N = int(input())
x = []
y = []
for i in range(N):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

# 세점 있을 떄 삼각형 넓이
# S = 1/2 * | (x1y2 + x2y3 + x3y1) - (x2y1 + x3y2 + x1y3)|

res = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            res = max(res, abs((x[i] * y[j] + x[j] * y[k] + x[k] * y[i]) 
                    - (x[j] * y[i] + x[k] * y[j] + x[i] * y[k])))
print(res/2)
