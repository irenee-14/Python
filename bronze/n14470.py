'''
2024.12.15
14470 - 전자레인지
'''

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if a < 0:
    time = -a * c + d + b * e
else:
    time = (b - a) * e

print(time)