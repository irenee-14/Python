'''
2023.2.1
1193 - 분수찾기
'''

# 1/1
# 1/2 2/1
# 3/1 2/2 1/3
# 1/4 2/3 3/2 4/1

n = int(input())

line = 1

while n > line:
    n -= line
    line += 1

x = n
y = line - n + 1

if line % 2 == 0:
    print(x, '/', y, sep='')
else:
    print(y, '/', x, sep='')