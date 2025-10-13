'''
2025.10.13
15923 - 욱제는 건축왕이야!!
'''

x, y = [], []
for _ in range(int(input())):
    a, b = map(int, input().split())
    x.append(a); y.append(b)
print((max(x)-min(x) + max(y)-min(y))*2)