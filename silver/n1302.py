'''
2024.5.20 
1302 - 베스트셀러
'''
N = int(input())
book = {}

for i in range(N):
    name = input()
    if name not in book:
        book[name] = 1
    else:
        book[name] += 1
        
M = max(book.values())
res = []

for k, v in book.items():
    if v == M:
        res.append(k)

res.sort()
print(res[0])
