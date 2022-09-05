'''
2562 - 최대값
2022.9.5
'''

num = []
for i in range(9):
    num.append(int(input()))
print(max(num))
print(num.index(max(num)) + 1)
