'''
2024.4.29
1568 - 새
'''
N = int(input())

k = 1
sec = 0
while N > 0:
    if N < k:
        k = 1
    N -= k 
    k += 1
    sec += 1
print(sec)ㅁ
