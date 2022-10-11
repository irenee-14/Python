'''
2022.10.11
2839 - 설탕배달
'''
N = int(input())

res = 0

while N >= 0:
    if N % 5 == 0:
        res += int(N//5)
        print(res)
        break
    N -= 3
    res += 1 
else:
    print(-1)
