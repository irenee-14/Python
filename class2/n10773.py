'''
2022.10.21
10773 - 제로
'''

k = int(input())
num = list()

for i in range(k):
    tmp = int(input())
    if tmp == 0:
        num.pop()
    else:
        num.append(tmp)
print(sum(num))