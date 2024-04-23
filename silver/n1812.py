'''
2024.4.23 
1812 - 사탕
'''
# a b c d e
# a + b 
# b + c 
# c + d 
# d + e 
# e + a
# (a + b) - (b + c) + (c + d) - (d + e) + (e + a) 
# = 2a 

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
    
res = []

first = 0
for i in range(len(arr)):
    if i % 2 == 0:
        first += arr[i]
    else: 
        first -= arr[i]
first = first//2

res.append(first)

for i in range(N - 1):
    res.append(arr[i] - res[i])
print(*res, sep="\n")
